from flask import Flask

from src import create_app

app = create_app()
# app = Flask(__name__)

# app.config['MONGO_URI'] = os.environ.get('DB_URI')
app.run()

@app.route("/")
def hello():
    return "Hello, World!"