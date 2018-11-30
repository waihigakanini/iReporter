from flask import Flask, Blueprint
from flask_restful import Api, Resource
from .views import RedFlags


version_one = Blueprint ('v1', __name__, url_prefix='/api/v1')

#app = Flask(__name__)
api = Api(version_one)

api.add_resource(RedFlags, '/red-flags')  

