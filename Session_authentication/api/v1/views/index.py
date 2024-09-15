#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return "OK"

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ GET /api/v1/unauthorized
    Return:
      - Unauthorized error
    """
    abort(401)

@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """ GET /api/v1/forbidden
    Return:
      - Forbidden error
    """
    abort(403)
