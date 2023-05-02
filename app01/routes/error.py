from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound

error_bp = Blueprint('error', __name__, url_prefix='/error')

@error_bp.app_errorhandler(NotFound)
def handle_not_found(err):
    return jsonify({'message': 'Resource not found'}), 404

@error_bp.app_errorhandler(Exception)
def handle_generic_exeption(err):
    return jsonify({'message': 'Unknown error'}), 500