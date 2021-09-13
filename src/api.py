from http import HTTPStatus
from flask import request, redirect
from flask_restful import Resource


class URLShortener(Resource):
    def post(self):
        data = request.get_json()
        url = data.get('url', None)
        if url is None or url == "":
            return "URL not given.", HTTPStatus.BAD_REQUEST

        # db_data = add_url(url)
        # id = db_data.inserted_id
        # return BASE_URL + str(id)
        return "Your URL was " + str(url)


class URLRedirect(Resource):
    def get(self, id):
        # data = get_url(id)
        # if data:
        #     url = data['url']
        #     if not url.startswith(('http://', 'https://')):
        #         url = 'http://' + url
        #     return redirect(url, code=HTTPStatus.PERMANENT_REDIRECT)
        # else:
        #     return "URL not found.", HTTPStatus.BAD_REQUEST

        return "Your Id was " + str(id)