from flask import request
from flask_restplus import Resource

from ..util.dto import ConfigDto

from ..service.configuration_service import retrieve_config
from ..util.decorator import token_required

api = ConfigDto.api


@api.route('')
class RetrieveConfiguration(Resource):
    @api.response(200, 'Successfully retrieved configuration')
    @api.doc('Retrieve a config from the server')
    @token_required
    def get(self):
        """Returns a configuration """
        data = request.json
        return retrieve_config()
