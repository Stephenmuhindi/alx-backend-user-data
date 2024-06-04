#!/usr/bin/env python3
"""
Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """
    api status
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """
    number gotten(stats)
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def abort_401() -> str:
    """
    test unauthorized api endpoint
    """
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def abort_403() -> str:
    """
    test forbiden api endpoint
    """
    abort(403)