from flask import render_template
from app import app
from .request import get_movies, get_movie

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

@app.route('/movie/<int:id>')
def movie(id):
    '''
    View detail movie page function that returns movie details page and it's data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'

    return render_template('movie.html', title = title, movie = movie)