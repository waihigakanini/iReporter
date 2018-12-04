from flask_restful import Resource
from flask import jsonify, make_response, request, abort
from .models import RedFlagModel

import datetime 

incidents = []

class RedFlags(Resource):
    """class for RedFlags"""
    
    def __init__(self):
        self.db = RedFlagModel()

    def get(self):
        """method for getting all a redflag record"""
        self.db.get_all()      
        return make_response(jsonify({
            "status" : 200,
            "data" : self.db.get_all()
        }), 200) 

    def post(self):        
        """method for posting a redflag record"""
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
    """class of RedFlag"""
    def __init__(self):
        self.db = RedFlagModel()
    def get(self, redflag_id):
        """method for getting a redflag record"""
        incident = self.db.find(redflag_id)
        if incident == None:
            return make_response(jsonify({
                "status" : 404,
                "error" : "Red flag does not exist"
            }), 404)
        return make_response(jsonify({
                    "status" : 200,
                    "data" : incident
                }), 200)

    def delete(self, redflag_id):
        """method for deleting a redflag record"""
        incident = self.db.find(redflag_id)
        if incident == None:
            return make_response(jsonify({
                "status" : 404,
                "error" : "Red flag does not exist"
            }), 404)
        self.db.delete(incident)
        success_message = {
            "id" : redflag_id,
            "data" : "red-flag record has been deleted"
        }
        return make_response(jsonify({
            "status": 200,
            "data" : success_message}))

    def put(self, redflag_id):
        """method for editing contents of a redflag record"""
        incident = self.db.find(redflag_id)
        if incident:
                     incident['location'] = request.json.get('location', incident['location'])
                     incident['createdBy'] = request.json.get('createdBy', incident['createdBy'])
                     incident['title'] = request.json.get('title', incident['title'])
                     incident['comment'] = request.json.get('comment', incident['comment'])
                     #incident['images'] = request.json.get('images', incident['images'])
                     #incident['videos'] = request.json.get('videos', incident['videos'])

                     success_message = {
                         "id" : redflag_id,
                         "message" : "Updated red-flag record"
                     } 
                     return make_response(jsonify({
                         "status" : 200,
                         "data" : success_message
                     }), 200)
        else:
            return {'error': 'Red flag does not exist', 'status': 404}

class EditRedflagLocation(Resource):
    """class for Update location of redflag class"""
    def __init__(self):
        self.db = RedFlagModel()
    def patch(self,redflag_id):
        """method for updating location of redflag a redflag record"""
        incident = self.db.find(redflag_id)
        if incident:
                     incident['location'] = request.json.get('location', incident['location'])
                     success_message = {
                         "id" : redflag_id,
                         "message" : "Updated red-flag records location"
                     } 
                     return make_response(jsonify({
                         "status" : 200,
                         "data" : success_message
                     }), 200)
        else:
            return {'error': 'Red flag does not exist', 'status': 404}
class EditRedflagComment(Resource):
    """class for update comment for a redflag record class"""
    def __init__(self):
        self.db = RedFlagModel()
        
    def patch(self,redflag_id):
        """method for updating comment of  a redflag record"""
        incident = self.db.find(redflag_id)
        if incident:
            incident['comment'] = request.json.get('comment', incident['comment'])
            success_message = {
                "id" : redflag_id,
                "message" : "Updated red-flag records comment"
            } 
            return make_response(jsonify({
                "status" : 200,
                "data" : success_message
            }), 200)
        else:
            return {'error': 'Red flag does not exist', 'status': 404}

    
