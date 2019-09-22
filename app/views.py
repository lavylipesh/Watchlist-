from flask import render_template
from app import app
from .requests import get_movies

@app.route('/')
def index():
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title ='Welcome to Watchlist'
    return render_template('index.html',title=title,popular=popular_movies,upcoming=upcoming_movie,now_showing_movie=now_showing_movie)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    return render_template('movie.html',id=movie_id)    