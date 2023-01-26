
from flask_restx import Api
from .user.views import api as user
from src.auth.views import api as auth
authorizations = {
    'Token Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}


api = Api(
    title='Flask API',
    description='Mulit Vendor Api',
    security='Token Auth',
    # doc='/documentations/',
    authorizations=authorizations
)

def connect_blueprint(app): 
    api.add_namespace(user, path="/user/")
    api.add_namespace(auth, path="/auth/")
    api.init_app(app)
