#!/usr/bin/env python
from app import create_app

app = create_app()


@app.route("/")
def hello():
    return "Hello, World!"
