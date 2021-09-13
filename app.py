from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from src.api import URLShortener

from src import create_app

# app = create_app()
# app = Flask(__name__)

# app.config['MONGO_URI'] = os.environ.get('DB_URI')


app = Flask(__name__)

api = Api(app)
CORS(app)
api.add_resource(URLShortener, '/')

app.run()

# @app.route("/")
# def hello():
#     return "Hello, World!"