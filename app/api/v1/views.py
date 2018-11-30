from flask_restful import Resource
from flask import jsonify, make_response, request, abort
from .models import RedFlagModel

import datetime 

incidents = []

class RedFlags(Resource):
    """docstring for RedFlags"""
    
    def __init__(self):
        self.db = RedFlagModel()

    def get(self):
        self.db.get_all()      
        return make_response(jsonify({
            "status" : 200,
            "data" : self.db.get_all()
        }), 200) 
       
