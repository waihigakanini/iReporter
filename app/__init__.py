from flask import Flask ,Blueprint


from .api.v1 import version_one as v1

def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)
    return app
