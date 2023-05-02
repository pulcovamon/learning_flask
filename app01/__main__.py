from app01 import create_app
from flask import jsonify, request, Response

app = create_app()

if __name__ == '__main__':
    app.run(host="127.0.0.1")