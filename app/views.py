from flask import render_template
from app import app

base_url = '/fluffymomo'


@app.route(base_url + '/')
@app.route(base_url + '/<int:comic_id>')
def index(comic_id=1):
    nav = {
        'prev': True if comic_id > 1 else False,
        'next': True if comic_id < 12 else False
    }
    comic = {
        'img': 'no' + str(comic_id) + '.jpg',
        'id': comic_id
    }

    return render_template(
        'index.html',
        title='The Adventures of Fluffy & Momo',
        nav=nav,
        comic=comic
    )
