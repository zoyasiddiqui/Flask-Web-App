# creating this file turns this website into a package

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "random"

    return app