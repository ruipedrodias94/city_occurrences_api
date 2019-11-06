
"""
.. module:: errors
   :synopsis: Error handling
.. moduleauthor:: Rui Dias <https://github.com/ruipedrodias94>
"""

from flask import jsonify, Blueprint
import os

error_handler = Blueprint("error_handler", __name__)


@error_handler.errorhandler(403)
def forbidden(e, description):
    """
    Handles the error 403
    """

    return jsonify(code=str(e), description=description), 403

@error_handler.errorhandler(404)
def resource_not_found(e, description):
    """
    Handles the error 404
    """

    return jsonify(code=str(e), description=description), 404

@error_handler.app_errorhandler(500)
def error_500(e, description):
    """
    Handles the error 500
    """

    return jsonify(code=str(e), description=description), 500
