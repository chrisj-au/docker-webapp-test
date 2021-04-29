import os
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/api/service-test')
def get_request():
    return "service-test works"

@app.route('/api/service-test/<key>')
def abn(key):
    return f'Your key is: {key}'

@app.route('/status')
@app.route('/api/service-test/status')
def get_status():
    return "Test Service: OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
