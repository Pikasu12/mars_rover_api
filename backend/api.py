from flask import Flask
from flask_restful import Resource, Api
import base64

app = Flask(__name__)
api = Api(app)

class MarsRoverAPI(Resource):
    def get(self):
        image_file = None

        with open("sample_image.jpg", "rb") as f:
            image_file = base64.b64encode(f.read())

        image_list = {"name": "sample_image", "image_file": image_file}
        return image_list

api.add_resource(MarsRoverAPI, '/')

if __name__ == '__main__':
    app.run(debug=True)