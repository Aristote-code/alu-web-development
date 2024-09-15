#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """ Returns API status """
    response = make_response("OK")
    response.headers['Content-Type'] = 'text/plain'
    return response

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
