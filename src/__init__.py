# from flask import Flask
# from flask_restful import Api
# # from flask_cors import CORS
# # from src.api import URLShortener
# from src.api import URLShortener, URLRedirect
# import src.api
#
# def create_app():
#
#     app = Flask(__name__)
#
#     api = Api(app)
#     # CORS(app)
#
#
#     api.add_resource(URLShortener, '/')
#     api.add_resource(URLRedirect, '/<id>')
#
#     return app
