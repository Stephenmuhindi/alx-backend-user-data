#!/usr/bin/env python3
"""
module defined hun
"""
from flask import abort, request
from api.v1.auth.auth import Auth
from typing import Tuple, TypeVar
import uuid
from models.user import User


class SessionAuth(Auth):
    """ here lives the session """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ new session """
        if not user_id:
            return None
        if type(user_id) != str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ userid of the session """
        if session_id is None:
            return None
        if type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ is it this current user """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """ mem clear """
        if request is None:
            return False
        sess_id = self.session_cookie(request)
        if not sess_id:
            return False
        user_id = self.user_id_for_session_id(sess_id)
        if not user_id:
            return False
        del self.user_id_by_session_id[sess_id]
        return True