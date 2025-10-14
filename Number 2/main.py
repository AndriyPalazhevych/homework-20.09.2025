from flask import Flask, render_template, abort, redirect, url_for
import random

app = Flask(__name__)

movies = {
    1: {"title": "Втеча з Шоушенка", "description": "Надихаюча історія про надію та волю."},
    2: {"title": "Хрещений батько", "description": "Кримінальна драма про мафіозну сім’ю Корлеоне."},
    3: {"title": "Шрек 1", "description": "Захоплюючі пригоди шрека та віслюка"},
    4: {"title": "Воно 1", "description": "Фільм розповідає про сімох дітей, яких тероризує невідома істота, що черпає силу зі страху, ненависті і розчарування."},
    5: {"title": "Кошмар на вулиці в'язів", "description": "Фільм зображає історію групи старшокласників, яким сниться той самий кошмар про потворного вбивцю з лезами на рукавиці. Сни з ним загадковим чином мають наслідки в реальності."},
}

@app.route('/')
def index():
    return render_template('index.html', movies=movies)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    movie = movies.get(movie_id)
    if movie:
        return render_template('movie.html', movie=movie, movie_id=movie_id)
    else:
        abort(404)

@app.route('/random')
def random_movie():
    movie_id = random.choice(list(movies.keys()))
    return redirect(url_for('movie', movie_id=movie_id))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
