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
    def delete(self, redflag_id):
        incident = self.db.find(redflag_id)

        self.db.delete(incident)
        success_message = {
            "id" : redflag_id,
            "data" : "red-flag record has been deleted"
        }

        return make_response(jsonify({
            "status": 200,
            "data" : success_message}))


class EditRedflagLocation(Resource):
    def __init__(self):
        self.db = RedFlagModel()
        
    def patch(self,redflag_id):
        incident = self.db.find(redflag_id)

        if incident:
                     
                     incident['location'] = request.json.get('location', incident['location'])

                     success_message = {
                         "id" : redflag_id,
                         "message" : "Updated red-flag records location"
                     } 
                     return make_response(jsonify({
                         "status" : 201,
                         "data" : success_message
                     }), 201)

            

        else:
            return {'error': 'Red flag does not exist', 'status': 404}
class EditRedflagComment(Resource):
    def __init__(self):
        self.db = RedFlagModel()
        
    def patch(self,redflag_id):
        incident = self.db.find(redflag_id)

        if incident:
                     
                     incident['location'] = request.json.get('location', incident['location'])

                     success_message = {
                         "id" : redflag_id,
                         "message" : "Updated red-flag records location"
                     } 
                     return make_response(jsonify({
                         "status" : 201,
                         "data" : success_message
                     }), 201)

            

        else:
            return {'error': 'Red flag does not exist', 'status': 404}

    
# def put(self, redflag_id):
#         data = {
#             'id' : redflag_id,
#             'createdOn' : datetime.datetime.utcnow(),
#             'createdBy' : request.json['createdBy'],
#             'type' : 'red-flags',
#             'location' : request.json['location'],
#             'status' : "Under Investigation",
#             # 'images' : request.json['images'],
#             # 'videos' : request.json['videos'],
#             'title' : request.json['title'],
#             'comment' : request.json['comment']
#         }

#         incident = self.db.find(redflag_id)

#         if incident:

#                 incident['createdBy'] = request.json.get('createdBy', incident['createdBy'])
#                 incident['location'] = request.json.get('location', incident['location'])
#                 # incident['images'] = request.json.get('images', incident['images'])
#                 # incident['videos'] = request.json.get('videos', incident['videos'])
#                 incident['title'] = request.json.get('title', incident['title'])
#                 incident['comment'] = request.json.get('comment', incident['comment'])

#                 success_message = {
#                     "id" : redflag_id,
#                     "message" : "Red-flag has been updated"
#                 }

#                 return make_response(jsonify({
#                     "status" : 201,
#                     "data" : success_message
#                 }), 201)
#         return make_response(jsonify({
#             "status" : 404,
#             "error" : "Red-flag does not exist"
#         }), 404)

       
       