from flask import Flask ,Blueprint
# from flask_restful import Api


from .api.v1 import version_one as v1

def create_app():
    app = Flask(__name__)
    # api = Api(app)
    app.register_blueprint(v1)

   
    # api.add_resource(RedFlags, '/api/v1/red-flags')  
    # api.add_resource(RedFlag, '/api/v1/red-flags/<int:redflag_id>') 
    return app
