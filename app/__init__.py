from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

app = Flask(
    __name__,
    instance_relative_config=True,
    static_url_path='/fluffymomo/static'
)

# Load default config and then instance config
app.config.from_object('config')
app.config.from_pyfile('config.py')

app.wsgi_app = ProxyFix(app.wsgi_app)

from app import views
