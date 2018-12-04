from flask import Flask, Blueprint
from flask_restful import Api, Resource
from .views import RedFlags, RedFlag, EditRedflagLocation, EditRedflagComment
from .routes import version_one as v1

version_one = Blueprint ('v1', __name__, url_prefix='/api/v1')
app = Flask(__name__)
api = Api(version_one)

