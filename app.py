from flask import Flask

app = Flask(__name__)
# app.config['MONGO_URI'] = os.environ.get('DB_URI')


@app.route("/")
def hello():
    return "Hello, World!"
