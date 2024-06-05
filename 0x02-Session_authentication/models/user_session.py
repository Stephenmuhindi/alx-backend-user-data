#!/usr/bin/env python3
"""
module for the user
"""
import hashlib
from models.base import Base


class UserSession(Base):
    """ User class
    """

    def __init__(self, *args: list, **kwargs: dict):
        """ user instantiation"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')