from flask_restful import Resource
from flask import jsonify, make_response, request, abort
from .models import RedFlagModel

import datetime 

incidents = []

class RedFlags(Resource):
    """docstring for RedFlags"""
    
   
    
    def post(self):        
        data = {
            'createdOn' : datetime.datetime.utcnow(),
            'createdBy' : request.json['createdBy'],
            'type' : 'red-flags',
            'location' : request.json['location'],
            'status' : "Under Investigation",
            # 'images' : request.json['images'],
            # 'videos' : request.json['videos'],
            'title' : request.json['title'],
            'comment' : request.json['comment']
        }
        self.db.save(data)
        
        success_message = {
            'message' : 'Thank You for Creating a Red-Flag'
        }

        return make_response(jsonify({
            "status" : 201,
            "data" : success_message
        }), 201)
    
