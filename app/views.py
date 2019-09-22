from flask import render_template
from app import app

@app.route('/')
def index():
    message ='Watchlist'
    return render_template('index.html',message=message)