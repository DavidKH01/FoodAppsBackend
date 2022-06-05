from flask import Flask
from flask_restful import Resource, Api
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

app = Flask(__name__)  # Flask app instance initiated
api = Api(app)  # Flask restful wraps Flask app around it.
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Food App',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)


class AwesomeResponseSchema(Schema):
    message = fields.Str(default='Success')


class AwesomeRequestSchema(Schema):
    api_type = fields.String(required=True, description="API type of awesome API")


#  Restful way of creating APIs through Flask Restful
class AwesomeAPI(MethodResource, Resource):
    @doc(description='My First GET Awesome API.', tags=['Awesome'])
    @marshal_with(AwesomeResponseSchema)  # marshalling
    def get(self):
        '''
        Get method represents a GET API method
        '''
        message = 'hello there'
        return {'message': message}

    @doc(description='My First GET Awesome API.', tags=['Awesome'])
    @use_kwargs(AwesomeRequestSchema, location=('json'))
    @marshal_with(AwesomeResponseSchema)  # marshalling
    def post(self, **kwargs):
        '''
        Get method represents a GET API method
        '''
        return {'message': 'My First Awesome API'}


class TestResponseSchema(Schema):
    message = fields.Str(default='Success')


class TestAPI(MethodResource, Resource):
    @doc(description='Test API', tags=['Test'])
    @marshal_with(TestResponseSchema)  # marshalling
    def get(self):
        '''
        Get method represents a GET API method
        '''
        return {'message': 'Test is working!'}


api.add_resource(AwesomeAPI, '/awesome')
docs.register(AwesomeAPI)

api.add_resource(TestAPI, '/test')
docs.register(TestAPI)

if __name__ == '__main__':
    app.run(debug=True)