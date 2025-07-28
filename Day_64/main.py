from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, URL
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNmI2Mjg2OWY4YTdhZDA0ZmVmOWZkYWEzZjhlMjZiYiIsIm5iZiI6MTc1MzY1ODAyOC4yNjQsInN1YiI6IjY4ODZiMmFjY2QwYTBkNzg4NGY3OGRmOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.j-eSTmHu4cnQ9lZh_g3iiT7sZjrCM8mKkPz1Dx8RhkM'
URL = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"


headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}


Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies.db'
db.init_app(app)


# CREATE TABLE
class BestMovies(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year : Mapped[int] = mapped_column(Integer, nullable=False)
    description : Mapped[str] = mapped_column(String(250), nullable=False) 
    rating : Mapped[float] = mapped_column(Float, nullable=True) 
    ranking : Mapped[int] = mapped_column(Integer, nullable=True)
    review : Mapped[str] = mapped_column(String(250), nullable=True)
    img_url : Mapped[str] = mapped_column(String(250), nullable=False)
    
# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# Rating a new movie
class RateMovieForm(FlaskForm):
    new_rating = FloatField('Your Rating out of 10 e.g. 8.5', validators=[DataRequired()])
    # location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    new_review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')

# CREATING A NEW RECORD TO THE DATABASE
class AddMovieForm(FlaskForm):
    movie = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    result = db.session.execute(db.select(BestMovies).order_by(BestMovies.rating))
    all_movies = result.scalars().all()
    
    all_ratings = [movie.rating for movie in all_movies if movie.rating is not None]
    i = len(all_ratings)
    for rating in all_ratings:        
        movies_to_update = db.session.execute(db.select(BestMovies).filter_by(rating=rating)).scalars().all()
        for movie in movies_to_update:
            movie.ranking = i
        i -= 1
    
    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=['GET', 'POST'])
def add():    
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_to_search = form.movie.data
        parameters = {'query': movie_to_search}     # API parameter for movie request
        response = requests.get(URL, headers=headers, params=parameters)
        all_movies = response.json()['results']   
        
        return render_template("select.html", options=all_movies)
        
    return render_template("add.html", form=form)
@app.route('/find')
def find_movie():
    result = db.session.execute(db.select(BestMovies).order_by(BestMovies.rating))
    all_movies = result.scalars().all()
    all_movie_title = [movie.title for movie in all_movies]     # getting all the movie titles from our database to check
    
    movie_id = request.args.get('id')
    movie_image_url = 'https://image.tmdb.org/t/p/w500'
    if movie_id:
        ID_URL = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
        id_response = requests.get(ID_URL, headers=headers)
        data = id_response.json()
        
        if data["title"] in all_movie_title:      #checking if the current movie is already in our database to avoid errors
            return redirect(url_for('home'))
        else:
            new_movie = BestMovies(
                title=data["title"],
                year=data["release_date"].split("-")[0],    # getting rid of the months and day in the string
                img_url=f"{movie_image_url}{data['poster_path']}",
                description=data["overview"]
            )
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for('edit', id=new_movie.id))   #parsing the movie ID to the edit.html to easily get

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie_to_edit = db.get_or_404(BestMovies, movie_id)
    
    if form.validate_on_submit():
        movie_to_edit.rating = float(form.new_rating.data)
        movie_to_edit.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie_to_edit)

@app.route("/delete")
def delete():
    delete_id = request.args.get('id')
    movie_to_delete = db.get_or_404(BestMovies, delete_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)
