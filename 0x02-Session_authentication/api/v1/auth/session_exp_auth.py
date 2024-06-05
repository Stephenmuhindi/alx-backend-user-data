#!/usr/bin/env python3
"""
expiry thing
"""
from flask import abort, request
from api.v1.auth.session_auth import SessionAuth
import uuid
from models.user import User
import os
import datetime


class SessionExpAuth(SessionAuth):
    """ session is done expired like milk """

    def __init__(self):
        """ instantantiation"""
        try:
            duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            duration = 0
        self.session_duration = duration

    def create_session(self, user_id=None):
        """ session created here """
        sess_id = super().create_session(user_id)
        if sess_id is None:
            return None
        value = {
                'user_id': user_id,
                'created_at': datetime.datetime.now()
                }
        self.user_id_by_session_id[sess_id] = value
        return sess_id

    def user_id_for_session_id(self, session_id=None):
        """ session from user"""
        if session_id is None:
            return None
        val = self.user_id_by_session_id.get(session_id)
        if not val:
            return None
        user_id = val.get('user_id')
        sess_creation_time = val.get('created_at')

        if self.session_duration <= 0:
            return user_id

        if sess_creation_time is None:
            return None

        now = datetime.datetime.now()
        live_time = datetime.timedelta(seconds=self.session_duration)

        if now > sess_creation_time + live_time:
            return None

        return user_id
