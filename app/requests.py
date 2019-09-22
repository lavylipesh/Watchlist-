from app import app
import urllib.request,jsonfrom .models import movie

api_key = app.config['MOVIE_API_KEY']

base_url = app.config["MOVIE_API_BASE_URL"]

def get_movies(category):
    get_movies_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_movies_url)as url:
        get_movies_data = url.read()
        get-movies_response = json.loads(get_moves_data)
        movie_results = None
        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process-results(movie_results_list)

            return movie_results
