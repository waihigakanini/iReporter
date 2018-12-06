"""This module contains users routes"""
from flask_restful import Resource
from flask import jsonify, make_response, request, abort
from app.api.v1.models.users_model import UsersModel


import datetime 


class SignUp(Resource):
    """class for users"""
    def __init__(self):
        self.db = UsersModel()

    def login(self):        
        """method for creating a new user"""
        current_user = request.json['username']
        user = self.db.find_username(current_user)
        if user == None:
            data = {
            'firstname' : request.json['firstname'],
            'lastname' : request.json['lastname'],
            'othernames' : request.json['othernames'],
            'email' : request.json['email'],
            'phonenumber' : request.json['phonenumber'],
            'username' : request.json['username'],
            'registered' : datetime.datetime.utcnow(),
            'isAdmin' : False,

            }
            self.db.save(data)
            success_message = {
                'message' : 'Thank You for creating an account'
            }

            return make_response(jsonify({
                "status" : 201,
                "data" : success_message
            }), 201)
        
        else:
            return {'error': 'user already exists', 'status': 400}

         
            
    def get(self,user_id):
        """method for fetching one user"""
        user = self.db.find(user_id)
        if user == None:
            return make_response(jsonify({
                "status" : 404,
                "error" : "user does not exist"
            }), 404)
        return make_response(jsonify({
                    "status" : 200,
                    "data" : user
                }), 200)
    def put(self,user_id):
        """method for editing user details"""
        user = self.db.find(user_id)
        if user == None:

            data = {
            'firstname' : request.json['firstname'],
            'lastname' : request.json['lastname'],
            'othernames' : request.json['othernames'],
            'email' : request.json['email'],
            'phonenumber' : request.json['phonenumber'],
            'username' : request.json['username'],
            'registered' : datetime.datetime.utcnow(),
            'isAdmin' : False,

         }
            self.db.save(data)
            success_message = {
            'message' : 'Thank You for creating an account'
            }

            return make_response(jsonify({
             "status" : 201,
                "data" : success_message
            }), 201)


         
        elif user:
                     
                     user['firstname'] = request.json.get('location', incident['location'])
                     user['createdBy'] = request.json.get('createdBy', incident['createdBy'])
                     user['title'] = request.json.get('title', incident['title'])
                     user['comment'] = request.json.get('comment', incident['comment'])
                     user['images'] = request.json.get('images', incident['images'])
                     user['videos'] = request.json.get('videos', incident['videos'])

                     success_message = {
                         "id" : user_id,
                         "message" : "Updated user details"
                     } 
                     return make_response(jsonify({
                         "status" : 200,
                         "data" : success_message
                     }), 200)
       
       
    def delete(self, user_id):
        """method for deleting user"""
        user = self.db.find(user_id)
        if user == None:
            return make_response(jsonify({
                "status" : 404,
                "error" : "user does not exist"
            }), 404)
        self.db.delete(user)
        success_message = {
            "id" : user_id,
            "data" : "user has been deleted"
        }
        return make_response(jsonify({
            "status": 200,
            "data" : success_message}))
    def get(self):
        """method for getting all the users"""
        self.db.get_all()
        return make_response(jsonify({
            "status" : 200,
            "data" : self.db.get_all()
        }), 200) 
    
    

