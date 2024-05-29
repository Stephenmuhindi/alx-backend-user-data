#!/usr/bin/env python3
""" Password hashing and validation functions """
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes password with bcrypt (returns digest)"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks password against hashed password (returns True if match)"""
    return bcrypt.checkpw(password.encode(), hashed_password)
