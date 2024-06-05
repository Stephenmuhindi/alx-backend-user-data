#!/usr/bin/env python3
"""
does anyone else see cookie as vulgar
"""
from flask import abort, request
from typing import List, TypeVar
from models.user import User
import re
import os


class Auth:
    """ class teacher with cookie """

    def require_auth(
        self, path: str, excluded_paths: List[str]
    ) -> bool:
        """ test if auth is required """
        if path is None or not excluded_paths:
            return True

        if path[-1] != '/':
            path = path + '/'
        for pth in excluded_paths:
            if pth[-1] == '*':
                pth = pth[:-1] + '.*'
            if re.fullmatch(pth, path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ prefect auth """
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        if auth_header:
            return auth_header
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ doc str """
        return None

    def session_cookie(self, request=None):
        """ cookie is here"""
        if request is None:
            return None
        _my_session_id = os.getenv('SESSION_NAME')
        return request.cookies.get(_my_session_id)