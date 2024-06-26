"""
This is a flask app which serves as a 
notice when the server is down
"""

__version__ = '0.3.0'


import os
from flask import Flask,url_for

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        UPLOAD_FOLDER="/tmp",
        APP_ROOT=os.path.dirname(os.path.abspath(__file__)),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists

    from . import home
    app.register_blueprint(home.bp)

    return app
