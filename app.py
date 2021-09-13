import os
from flask import Flask

# from src import create_app
from flask_restful import Api
from flask_cors import CORS
from src.api import URLShortener, URLRedirect

# app = create_app()
app = Flask(__name__)
api = Api(app)
CORS(app)


app.config['MONGO_URI'] = os.environ.get('DB_URI')
# app.run()



# api.add_resource(HelloWorld, '/')
api.add_resource(URLShortener, '/')
api.add_resource(URLRedirect, '/<id>')

if __name__ == '__main__':
    app.run()

# @app.route("/")
# def hello():
#     return "Hello, World!"