from flask import Blueprint, jsonify, Response, request

users_bp = Blueprint('users', __name__, url_prefix='users')

@users_bp.route('', methods=['GET'])
def get_users():
    users = [{'name': 'John'}, {'name': 'Jane'}]
    return jsonify(users)

@users_bp.route('', methods=['POST'])
def create_user():
    d = request.json
    print(d)
    return Response(status=204)