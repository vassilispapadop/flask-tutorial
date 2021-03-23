from flask import Blueprint, request
from flask_restful import Api, Resource
from .resources import Video

# api = Blueprint('api', __name__)

class AppApi():
    def __init__(self, app):
        self.api = Api(app)
        # self.api_prefix = Blueprint('api', __name__)
        self.api.add_resource(Video, '/api/video')
