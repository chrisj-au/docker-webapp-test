import os
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/api/service-test')
def get_request():
    return "Some test text"

@app.route('/api/service-test/<key>')
def abn(key):
    if not key:
        abort(400)

    results = json.dumps("{'hi':'ok'}")
    return Response(response=json.dumps(results), mimetype='application/json')

@app.route('/status')
@app.route('/api/service-test/status')
def get_status():
    return "Service is OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)