#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello NGA!'

if __name__ == '__main__':
    app.run()
