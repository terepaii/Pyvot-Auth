from flask import request
from flask_restplus import Resource

from ..util.dto import RegisterDto
from ..service.register_service import save_new_user

api = RegisterDto.api
_user_register = RegisterDto.user_register


@api.route('/register')
class UserRegister(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user_register, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        print(data)
        return save_new_user(data=data)
