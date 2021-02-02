import json

from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

user = Blueprint('api', __name__, url_prefix='/api/user')


@user.route('/login', methods=['POST'])
def login():
    req = request.get_json()
    username = req['username']
    password = req['password']

    if username != 'admin' or password != 'password':
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(name="Aaron Kao", token=access_token,
                   avatar="https://lh3.googleusercontent.com/ogw/ADGmqu9WYCgH_k7sX1JPJHN7RddvsK6hLEcSCnOWmoTDUsE=s192"
                          "-c-mo")


@user.route('/logout', methods=['POST'])
def logout():
    return '{"status": "success"} '
