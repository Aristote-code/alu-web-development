#!/usr/bin/env python3
"""
Auth class
"""

import re
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a given path requires authentication.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        # Ensure path ends with a slash for consistent comparison
        path = path.rstrip('/') + '/'

        for excluded_path in excluded_paths:
            # Convert glob pattern to regex pattern
            pattern = excluded_path.replace('*', '.*').rstrip('/') + '/'
            if re.match(pattern, path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
        """
        return None
