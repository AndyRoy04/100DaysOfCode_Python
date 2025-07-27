from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book_library.db"     # Giving a name for our database, i.e. book_library.db
db = SQLAlchemy(model_class=Base)   # Create the extension
db.init_app(app)    # Initialise the app with the extension

class Book(db.Model):
    id: Mapped[str] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()  # I use the .scalars() to get the elements rather than entire rows from the database
        
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # CREATING THE RECORD        
        new_book = Book(
            title = request.form.get('title'), 
            author = request.form.get('author'), 
            rating = request.form.get('rating'))
        db.session.add(new_book)
        db.session.commit()
            
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']  # getting the ID parsed to the url
        book_to_edit = db.get_or_404(Book, book_id) # Use scalar_one_or_none for a single result
        book_to_edit.rating = request.form.get('rate')
        db.session.commit()

        return redirect(url_for('home'))
    book_id = request.args.get('id')
    print(book_id)
    book_to_edit = db.get_or_404(Book, book_id)
    return render_template('edit.html', book=book_to_edit)

@app.route('/delete')
def delete():
    delete_id = request.args.get('id')
    
    book_to_edit = db.get_or_404(Book, delete_id)
    db.session.delete(book_to_edit)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

