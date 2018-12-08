from flask import request, send_from_directory, abort

from . import app
from .my_hash import file_hash


@app.route('/tests/<filename>')
def check_version(filename):
    tests_folder = app.config['TESTS_FOLDER']
    req_file = tests_folder / filename

    if not req_file.exists():
        return abort(404)

    req_version = request.headers.get('If-None-Match')
    version = file_hash(req_file)
    if version == req_version:
        return '', 304

    return send_from_directory(tests_folder, filename)
