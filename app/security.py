from flask import abort

from flask_httpauth import HTTPBasicAuth

from . import app


auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == app.config['USERNAME']:
        return app.config['PASSWORD']
    return None

@auth.error_handler
def unauthorized():
    return abort(401)