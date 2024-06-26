#!/usr/bin/env python3
"""
documentation module
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ api status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ object number detail"""
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def abort_401() -> str:
    """ loss of life in womb"""
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def abort_403() -> str:
    """forbiden route"""
    abort(403)
