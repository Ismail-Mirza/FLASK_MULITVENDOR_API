
from flask_restx import Api
from .user.views import api as user
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
    # doc='/documentation',
    authorizations=authorizations
)

def connect_blueprint(app):
    
    api.add_namespace(user, path="/user/")
    api.init_app(app)
