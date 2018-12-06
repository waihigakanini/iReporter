"""This module creates a blueprint and registers the urls"""

from flask import Flask, Blueprint
from flask_restful import Api, Resource
from .incidents import RedFlags, RedFlag, EditRedflagLocation, EditRedflagComment
from .users import SignUp

version_one = Blueprint ('v1', __name__, url_prefix='/api/v1')

api = Api(version_one)

api.add_resource(RedFlags, '/red-flags', strict_slashes=False)  
api.add_resource(RedFlag, '/red-flags/<int:redflag_id>',strict_slashes=False) 
api.add_resource(EditRedflagLocation, '/red-flags/<int:redflag_id>/location',strict_slashes=False)
api.add_resource(EditRedflagComment, '/red-flags/<int:redflag_id>/comment',strict_slashes=False)
api.add_resource(SignUp, '/auth/signup',strict_slashes=False)
