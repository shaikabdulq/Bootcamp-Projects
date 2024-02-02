from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
API_KEY = "ENTER_API_KEY" # Enter API Key
Bootstrap5(app)

##CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy()
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title")
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

# Adding the Update functionality
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete", methods=["POST","GET"])
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie,movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET","POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get("https://api.themoviedb.org/3/search/movie",
                                params={"api_key": "ENTER_API_KEY",
                                        "query": movie_title})   # Enter API Key
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html",form=form)

@app.route("/find", methods=["GET", "POST"])
def find_movie():
    movie_id = request.args.get("id")
    url = "https://api.themoviedb.org/3/movie/"
    params = {
        "api_key": API_KEY
    }
    response = requests.get((url + movie_id), params=params)
    json_data = json.loads(response.text)
    title = json_data['title']
    img_url = "https://image.tmdb.org/t/p/w500" + json_data['poster_path']
    year = json_data['release_date'][:4]
    description = json_data['overview']
    new_movie = Movie(title=title,img_url=img_url,year=year,description=description)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('rate_movie', id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
