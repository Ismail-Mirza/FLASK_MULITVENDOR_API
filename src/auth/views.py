from flask_restx import Resource
from flask import request
from ..extension import bcrypt, db
from ..user.models import User
from sqlalchemy.exc import IntegrityError

