import os
from flask import Flask

from . import auth, sv

def create_app(test_config=None):
    # create and configure the app
    secret_key = os.environ['SECRET_KEY']
    app = Flask(__name__, instance_relative_config=True)
    app.debug = False
    app.config.from_mapping(
        SECRET_KEY=secret_key,
        debug=False
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.register_blueprint(auth.bp)
    app.register_blueprint(sv.bp)
    
    return app

# set FLASK_APP=app
# set FLASK_ENV=development
# flask run
