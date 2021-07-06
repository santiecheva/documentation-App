from app.common.error_handling import AppErrorBaseClass, ObjectNotFound
from flask import request

from flask_restful import  Resource

from .schemas import UserSchema
from .models import User


user_schema = UserSchema()


class UserListResource(Resource):
    def get(self):
        users = User.get_all()
        result = user_schema.dump(users, many=True)
        return result

    def post(self):
        data = request.get_json()
        user_dict = user_schema.load(data)
        user = User(
            username=user_dict['username'],
            email=user_dict['email']
        )
        user.save()
        response = user_schema.dump(user)
        return response, 201

class UserResource(Resource):
    def get(self, user_id):
        user = User.get_by_id(user_id)
        if user is None:
            raise ObjectNotFound('No existe el usuario')
        response = user_schema.dump(user)
        return response
