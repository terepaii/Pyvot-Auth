
from flask_restplus import Api
from flask import Blueprint

from .main.controller.auth_controller import api as auth_ns
from .main.controller.confguration_controller import api as config_ns
from .main.controller.register_controller import api as register_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS AUTHENTICATION API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(register_ns, path='/authentication')
api.add_namespace(auth_ns, path='/authentication')
api.add_namespace(config_ns, path='/configurations')