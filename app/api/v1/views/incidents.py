"""This module contains incidents routes"""
import re
from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from app.api.v1.models.incidents_model import RedFlagsModel


redflags_list = []
def check_empty(value):
    """function to check whether empty"""
    if not re.match(r"[A-Z1-9]+",value):
        raise ValueError("pattern not matched")
def comment_validator(value):
    """function to validate comment """
    if not re.match(r"[A-Z]",value):
        raise ValueError("pattern not matched")
def coordinate_validator(value):
    """function for validating coordinates"""
    if not re.match(r"^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$", value):
        raise ValueError("Pattern not matched")


parser = reqparse.RequestParser(bundle_errors = True)

parser.add_argument('createdby',type =check_empty, required= True, nullable= False , help="cannot be empty or contain a special case")


parser.add_argument('comment',type =comment_validator,required= True, nullable= False , help="Cannot contain a special character")


parser.add_argument('location',type =coordinate_validator,required= True, nullable= False , help="pattern not matched")

parser.add_argument('title',type =comment_validator,required= True, nullable= False , help="cannot special cases")

class RedFlags(Resource):
    """class for RedFlags"""
    def __init__(self):
        self.db = RedFlagsModel()
        """initializes the resource with a reference of the model it should use"""
    def get(self):

        """method for getting all redflag records"""
        data = self.db.get_all()
        if data == "none":
            return make_response(jsonify({
                "status" : 200,
                "message" : "There are no red-flags at the moment"
            }), 200)

        return make_response(jsonify({
            "status" : 200,
            "data" : data
        }), 200) 

    def post(self):

        """method for posting a redflag record"""
        json_data = request.get_json(force= True)
        if not json_data:
             return {'error': 'Kindly ensure you have inserted your details', 'status': 400}
        args = parser.parse_args()
        data = {
           'createdby': request.json['createdby'],
           'title': request.json['title'],
           'images': request.json.get('images'),
           'videos': request.json.get('videos'),
           'comment': request.json['comment'],
           'location': request.json['location'],
           'id': len(self.db.db)+1
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
            self.db = RedFlagsModel()
    """initializes the resource with a reference of the model it should use"""
    def get(self, redflag_id):
        """method for getting a redflag record"""
        incident = self.db.find(redflag_id)
        if incident == None:
            return make_response(jsonify({
                "status" : 200,
                "error" : "Red flag does not exist"
            }), 200)
        return make_response(jsonify({
                    "status" : 200,
                    "data" : incident
                }), 200)

    def delete(self, redflag_id):
        """method for deleting a redflag record"""
        incident = self.db.find(redflag_id)
        if incident == None:
            return make_response(jsonify({
                "status" : 200,
                "error" : "Red flag does not exist"
            }), 200)
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
                     incident['image'] = request.json.get('image', incident['image'])
                     incident['videos'] = request.json.get('videos', incident['videos'])
                     success_message = {
                         "id" : redflag_id,
                         "message" : "Updated red-flag record"
                     }
                     return make_response(jsonify({
                         "status" : 200,
                         "data" : success_message
                     }), 200)
        return {'error': 'Red flag does not exist', 'status': 200}

class EditRedflagLocation(Resource):
    """class for Update location of redflag class"""
    def __init__(self):
        """initializes the resource with a reference of the model it should use"""
        self.db = RedFlagsModel()
    def patch(self,redflag_id):
        """method for updating location of redflag a redflag record"""
        incident = self.db.find(redflag_id)
        if incident:
                     incident['location'] = request.json.get('location', "keyerror")
                     if incident['location'] == 'keyerror':
                         return make_response(jsonify({
                            "status" : 400,
                            "message " : "location key is required"
                         }), 400)
                     success_message = {
                         "id" : redflag_id,
                         "message" : "Updated red-flag records location"
                     }
                     return make_response(jsonify({
                         "status" : 200,
                         "data" : success_message
                     }), 200)
        return {
                'error': 'Red flag does not exist', 'status': 200}
class EditRedflagComment(Resource):
    """class for update comment for a redflag record class"""
    def __init__(self):
        self.db = RedFlagModel()

    def __init__(self):
        """initializes the resource with a reference of the model it should use"""
        self.db = RedFlagsModel()
    def patch(self,redflag_id):
        """method for updating location of redflag a redflag record"""
        incident = self.db.find(redflag_id)
        if incident:
                     incident['comment'] = request.json.get('comment', "keyerror")
                     if incident['comment'] == 'keyerror':
                         return make_response(jsonify({
                            "status" : 400,
                            "message " : "comment key is required"
                         }), 400)
                     success_message = {
                         "id" : redflag_id,
                         "message" : "Updated red-flag records comment"
                     }
                     return make_response(jsonify({
                         "status" : 200,
                         "data" : success_message
                     }), 200)
        return {
                'error': 'Red flag does not exist', 'status': 200}
