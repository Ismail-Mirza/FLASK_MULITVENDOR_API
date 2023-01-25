from flask_restx import Resource,Namespace
from flask import request
from ..extension import bcrypt
from .models import User
from sqlalchemy.exc import IntegrityError
from .helper.validators import UserValidators
from ..helpers import remove_space
from .helper.variable import normal_user
from src.user.helper.schema import UserSchema
from src.exceptions.responses import success_response, error_response
from flask_jwt_extended import verify_jwt_in_request,decode_token
from src.helpers.send_mail import send_email






api = Namespace('user', description='user related operations')
signup_model = api.model("signup",normal_user)

@api.route("register/")
class userView(Resource):
    def get(self):
        return {"message":"m"},200
    @api.expect(signup_model)
    def post(self):
        try:
            data = request.get_json()
            #validate data
            UserValidators.validate(data)
            data = remove_space(data)
            data['password'] = bcrypt.generate_password_hash(data.get("password"))
            new_user = User(**data)
            # new_user.save()
            user_schema = UserSchema()
            user_data = user_schema.dump(new_user)
            # print(user_data)
            send_email(user_data, 'Confirmation Email', 'confirmation_email.html')

            return {
                'status': 'success',
                'message': 'User successfully created. Please check your email to continue.'
            }, 201
        except IntegrityError:
            return {"message": "Email is already existed."}, 409


@api.route('activate/<string:token>',endpoint="activate")
class UserActivateView(Resource):
    """" Resource class for user account activation endpoint """

    def get(self, token):
        """ Endpoint to activate the user account """

        user = decode_token(token)
        print(token)
        if user is None:
            error_response['message'] = 'Account activation token is invalid'
            return error_response, 400

        if user.is_activated:
            error_response['message'] = 'User account already activated'
            return error_response, 400

        user.update({'is_activated': True})
        # user_cart = Cart(user_id=user.id)
        # user_cart.save()

        return {
            'status': 'success',
            'message': 'User successfully activated'
        }, 200
