from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page that returns the index page and it's content
    '''
    message = 'Hello World from Fred Ojure!!!!!'
    return render_template('index.html', message = message)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View detail of a movie gien a movie id
    '''
    return render_template('movie.html', id=movie_id)