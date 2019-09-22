from flask import render_template
from app import app

@app.route('/')
def index():
    title =''
    return render_template('index.html',title=title)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    return render_template('movie.html',id=movie_id)    