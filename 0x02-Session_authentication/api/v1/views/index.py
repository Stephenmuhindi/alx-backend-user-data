#!/usr/bin/env python3
""" 
Module documentation
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ 
    api status get method
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """
    object number tallied
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def abort_401() -> str:
    """
    get method for api unauthorized route
    """
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def abort_403() -> str:
    """
    get method for api forbidden route
    """
    abort(403)