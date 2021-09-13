# import os
# from http import HTTPStatus
# from flask import request, redirect
# from flask_restful import Resource

# from src.db import add_url, get_url


# BASE_URL = os.environ.get('BASE_URL')


# class URLShortener(Resource):
#     def get(self):
#         return "You called get on /", HTTPStatus.OK


    # def post(self):
    #     data = request.get_json()
    #     url = data.get('url', None)
    #     if url is None or url == "":
    #         return "URL not given.", HTTPStatus.BAD_REQUEST

    #     # db_data = add_url(url)
    #     # id = db_data.inserted_id
    #     # return BASE_URL + str(id)
    #     return "post call seen", HTTPStatus.OK


# class URLRedirect(Resource):
#     def get(self, id):
#         # data = get_url(id)
#         # if data:
#         #     url = data['url']
#         #     if not url.startswith(('http://', 'https://')):
#         #         url = 'http://' + url
#         #     return redirect(url, code=HTTPStatus.PERMANENT_REDIRECT)
#         # else:
#         #     return "URL not found.", HTTPStatus.BAD_REQUEST

#         return "get call seen", HTTPStatus.OK
