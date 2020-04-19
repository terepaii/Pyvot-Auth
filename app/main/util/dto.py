from flask_restplus import Namespace, fields


class RegisterDto:
    api = Namespace('register', description='register operation')
    user_register = api.model('register', {
        'Login': fields.String(required=True, description='user\'s username'),
        'Password': fields.String(required=True, description='user password'),
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'Login': fields.String(required=True, description='The user\'s name'),
        'Password': fields.String(required=True, description='The user password '),
    })

class ConfigDto:
    api = Namespace('config', description='configuration related operations')
    user_config = api.model('config', {})
