from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os

load_dotenv()
OMDB_APIKEY = (os.getenv('OMDB_APIKEY'))
OMDB_ENDPOINT = (os.getenv('OMDB_ENDPOINT'))

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(2500), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)

"""new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=4,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=2,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)

# Create table schema in the database. Requires application context.
with app.app_context():
    db.session.add(new_movie)
    db.session.add(second_movie)
    db.session.commit()"""

class UpdateForm(FlaskForm):
    rating = SelectField(label="Your rating (1 to 5)",choices=[1,2,3,4,5], validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()], render_kw={'size': 50})    
    submit = SubmitField(label="Confirm")

class AddForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()], render_kw={'size': 50})    
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_movies = result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/update", methods=["GET", "POST"])
def update():    
    if request.method == "POST":
        # UPDATE RECORD
        movie_id = request.args.get('id')
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.rating = request.form["rating"]
        movie_to_update.review = request.form["review"]
        db.session.commit()
        return redirect(url_for('home'))
    movie_id = request.args.get('id')
    movie_rating = request.args.get('rating')
    movie_review = request.args.get('review')
    movie_selected = db.get_or_404(Movie, movie_id)
    form = UpdateForm(rating=movie_rating, review=movie_review)
    return render_template("edit.html", movie=movie_selected, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    # DELETE A RECORD BY ID
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        movie_title = request.form["title"]
        return redirect(url_for('select', title=movie_title))
    form = AddForm()
    return render_template("add.html", form=form)


@app.route("/select", methods=["GET", "POST"])
def select():
    movie_title = request.args.get('title')
    params = {
        "apikey": OMDB_APIKEY,
        "s": movie_title,
        "type": "movie",
    }
    response = requests.get(OMDB_ENDPOINT, params=params)
    response.raise_for_status()
    all_movies = response.json()["Search"]
    movie_title = request.args.get('title')
    return render_template("select.html", movies=all_movies)


@app.route("/find", methods=["GET", "POST"])
def find():
    selected_movie_id = request.args.get('movie_id')
    print(selected_movie_id)
    
    params = {
        "apikey": OMDB_APIKEY,
        "i": selected_movie_id,
    }
    response = requests.get(OMDB_ENDPOINT, params=params)
    response.raise_for_status()
    movie_data = response.json()

    # CREATE RECORD
    new_movie = Movie(
        title = movie_data["Title"],
        year = movie_data["Year"],
        description = movie_data["Plot"],
        rating = 0,
        ranking = 0,
        review = "",
        img_url = movie_data["Poster"],
    )
    
    db.session.add(new_movie)
    db.session.commit()
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars().all()
    new_movie_id = all_movies[-1].id
    return redirect(url_for('update', id=new_movie_id, rating=0, review=' '))


if __name__ == '__main__':
    app.run(debug=True)
