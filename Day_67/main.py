from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)    # Linking the CKEditor Library to my app

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    
    # def to_dict(self):
    #     dictionary = {}
    #     for column in self.__table__.columns:
    #         dictionary[column.name] = getattr(self, column.name)    # Function to store all the raws as a key value pair in a dictionary
    #     return dictionary

# CREATING A NEW RECORD TO THE DATABASE
class NewPost(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    sub_title = StringField('Subtitle', validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('SUBMIT POST')

with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()

    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Retrieving a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route('/new_post', methods=["GET", "POST"])
def new_post():
    form = NewPost()
    # Getting the date
    today = date.today()
    today_date = today.strftime("%B %d, %Y")
    
    if form.validate_on_submit():
        post_to_add = BlogPost(
            title=form.title.data,
            subtitle=form.sub_title.data,
            date=today_date,
            author=form.author.data,
            img_url=form.img_url.data,
            body=form.body.data
        )
        db.session.add(post_to_add)
        db.session.commit()
        
        return redirect(url_for('get_all_posts'))
        
    return render_template('make-post.html', form=form)


@app.route("/edit_post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    # Auto-populating the form fields for an existing post
    edit_form = NewPost(
        title=requested_post.title,
        subtitle=requested_post.subtitle,
        img_url=requested_post.img_url,
        author=requested_post.author,
        body=requested_post.body
    )
    if edit_form.validate_on_submit():
        requested_post.title = edit_form.title.data
        requested_post.subtitle = edit_form.sub_title.data
        requested_post.author = edit_form.author.data
        requested_post.img_url = edit_form.img_url.data
        requested_post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=requested_post.id))
    
    return render_template('make-post.html', form=edit_form, edit=True)

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))
# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
