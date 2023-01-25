from flask import Blueprint,jsonify
from sqlalchemy.exc import IntegrityError
from ..extension import bcrypt,db
from datetime import timedelta
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_restx import Api
auth = Blueprint("auth",__name__,url_prefix="/auth/")
api = Api(auth,
          title='Ecomerce',
          version='1.0',
          description='A description',
          # All API metadatas
          )





# @auth.route("/register/",methods=["POST"])





# @auth.route("/seller/",methods=["POST"])
# def create_seller():
#     try:
#         data = request.get_json()
#         user = User(
#             email = data['email'],
#             password=bcrypt.generate_password_hash(data['password']),
#             is_seller = True,
#             is_admin =False,
#             is_employee =False
#         )
#         db.session.add(user)
#         db.session.commit()
#         return jsonify({"message":"User is successfully created"})
#     except IntegrityError:
#         return jsonify({"message":"Email is already existed."}),409


# @auth.route('/login/', methods=['POST'])
# def auth_login():
#     # Find a user by email address
#     # Build the query to select the user with the incoming email address.
#     user =User.query.filter_by(email=request.json['email']).first()
#     # If user exists (if user is truthy) and the incoming password is correct create a JWT token and return it.
#     if user and bcrypt.check_password_hash(user.password, request.json['password']):
#         # Timedelta is a function that allows a time period to be specified in any unit and it will calculate and return how many minutes that is. This token will expire after 5 days. # change this to one before deployment. Delta means difference.
#         token = create_access_token(identity=str(
#             user.id), expires_delta=timedelta(days=5))
#         # The token isn't stored on the server. Instead the server uses the secret key to validate the token.
#         # The payload of the token identifys the user.
#         return {'email': user.email, 'token': token}
#     else:
#         # For security reasons users are not told which one is incorrect. This prevents brute force attacks.
#         return {'error': 'Invalid email or password'}, 401


