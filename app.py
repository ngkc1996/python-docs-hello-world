from flask import Flask

# from src import create_app
from flask_restful import Api
from src.api import HelloWorld

# app = create_app()
app = Flask(__name__)
api = Api(app)

# app.config['MONGO_URI'] = os.environ.get('DB_URI')
# app.run()



api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()

# @app.route("/")
# def hello():
#     return "Hello, World!"