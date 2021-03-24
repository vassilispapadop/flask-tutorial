from flask import request, abort
from flask_restful import Resource
from marshmallow import Schema, fields

class VideoSchema(Schema):
    key = fields.String(required=True)

class Video(Resource):
    def __init__(self):
        # self.schema = kwargs['schema']
        self.schema = VideoSchema()

    def get(self):
        errors = self.schema.validate(request.args)
        if errors:
            abort(400, str(errors))

        return {'data':'Hello, world!'}