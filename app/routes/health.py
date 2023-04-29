from flask import Blueprint

health_pb = Blueprint('health', __name__)

@health_pb.route('/health', methods=['GET'])
def health():
    return 'OK'