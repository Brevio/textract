# -*- coding: utf-8 -*-
import six
from api import Ocr
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path="")
auth = HTTPBasicAuth()

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': 'hello'})

@app.route('/textract-gcqi/ocr', methods=['POST'])
def extract_text():
    data_json = request.json
    imagebase64 = data_json.get("fileBase64")
    fileName = data_json.get("fileName")
    ocr = Ocr()
    file_in = ocr.decode(imagebase64,fileName)
    return ocr.extract(file_in)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)
