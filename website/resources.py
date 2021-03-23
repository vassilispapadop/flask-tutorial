from flask_restful import Resource

class Video(Resource):
    def get(self):
        return {'data':'Hello, world!'}