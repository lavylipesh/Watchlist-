from flask import render_template
from app import app
from .requests import get_movies

@app.route('/')
def index():
    popular_movies = get_movies('popular')
    print(popular_movies)
    title ='Welcome to Watchlist'
    return render_template('index.html',title=title,popular=popular_movies)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    return render_template('movie.html',id=movie_id)    