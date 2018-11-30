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
    
class RedFlag(Resource):
    """docstring of RedFlag"""
    def __init__(self):
        self.db = RedFlagModel()
        
        # self.id = len(self.db) + 1
    def get(self, redflag_id):

        incident = self.db.find(redflag_id)
        return make_response(jsonify({
                    "status" : 200,
                    "data" : incident
                }), 200)
