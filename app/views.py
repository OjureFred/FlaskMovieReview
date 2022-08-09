from flask import render_template
from app import app
from .request import get_movies

#Views
@app.route('/')
def index():
    '''
    View root page that returns the index page and it's content
    '''
    #Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movies = get_movies('now_playing')
    print(popular_movies)

    title = 'Home - Welcome to the best Movie Reviews Website'

    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movies)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View detail of a movie gien a movie id
    '''
    
    return render_template('movie.html', id=movie_id)