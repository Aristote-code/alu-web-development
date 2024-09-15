#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort
from api.v1.views import app_views
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__)
app.register_blueprint(app_views)
auth = None

if getenv("AUTH_TYPE") == "basic_auth":
    auth = BasicAuth()

@app.before_request
def before_request():
    if auth:
        excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
        if auth.require_auth(request.path, excluded_paths):
            if auth.authorization_header(request) is None:
                abort(401)
            if auth.current_user(request) is None:
                abort(403)
    request.current_user = auth.current_user(request) if auth else None

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
