from flask import Flask, render_template
from flask_bootstrap import Bootstrap # pip install bootstrap-flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=15)])
    submit = SubmitField('Login')

app = Flask(__name__)
app.secret_key = "justfortesting"

bootstrap = Bootstrap(app)  # initialise bootstrap-flask 

EMAIL = 'admin@email.com'
PASSWORD = '12345678'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user_email = login_form.email.data
        user_password = login_form.password.data
        if user_email == EMAIL and user_password == PASSWORD:
            return render_template('success.html')
        else:
            return render_template('denied.html')
        print(user_email)
    return render_template('login.html', form=login_form)

# @app.route('/success')
# def success():
#     return render_template('success.html')

# @app.route('/denied')
# def denied():
#     return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
