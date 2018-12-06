from flask import Flask ,Blueprint
from .api.v1 import version_one as v1
from .api.v1.views.routes import version_one as v1
from flask import jsonify, make_response

def page_not_found(error):
    return make_response(jsonify({
        "status" : 404,
        "error" : "page not found"
    }), 404)


def create_app():
    """method for creating app"""
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found )
    app.register_blueprint(v1)
    return app
