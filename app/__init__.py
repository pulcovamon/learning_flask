from flask import Flask
from app.routes.health import health_pb
from app.routes.users import users_bp
from app.routes.error import error_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_pb)
    app.register_blueprint(users_bp)
    app.register_blueprint(error_bp)
    return app