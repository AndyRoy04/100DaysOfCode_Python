from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Creating a user_loader
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user_exist = db.session.execute(db.select(User).where(User.email == request.form['email'])).scalar()

        if user_exist:
            flash("You've already signed up with that email. Log in instead!")
            return redirect(url_for('login'))
        else:   
            new_user = User(
                email = request.form['email'],
                password = generate_password_hash(request.form['password'], method='pbkdf2', salt_length=8),    # Hashing the user generated password
                name = request.form['name'],
            )
            db.session.add(new_user)
            db.session.commit()
            
            login_user(new_user)
            flash('Registration was successful.')
            
            return render_template('secrets.html', name=request.form['name'])
    return render_template("register.html", logged_in=current_user.is_authenticated)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        # Find user by email entered.
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        
        # Checking stored password hash against entered password hashed.
        if not user:
            flash("This email doesn't exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):            
            flash('Wrong password. Please enter the correct password')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return render_template('secrets.html', logged_in=current_user.is_authenticated)
            
    return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf')

if __name__ == "__main__":
    app.run(debug=True)
