from flask import Blueprint, request
from flask_restful import Api
from .resources import Video


# api = Blueprint('api', __name__)

class AppApi():
    def __init__(self, app):
        self.api = Api(app)
        # schema = VideoSchema()
        # self.api.add_resource(Video, '/api/video/', resource_class_kwargs = {'schema': schema})
        self.api.add_resource(Video, '/api/video/')
        



