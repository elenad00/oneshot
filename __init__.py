from flask import Flask, app

def create_app(config_file=None, settings_override=None):
    app = Flask(__name__)
    return app

@app.route('/')
def index():
    return "Hello World"