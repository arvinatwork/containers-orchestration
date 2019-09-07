# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class HelloPUP(Resource):
    def get(self):
        return {'hello': 'PUP'}

api.add_resource(HelloWorld, '/')
api.add_resource(HelloPUP, '/pup')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')