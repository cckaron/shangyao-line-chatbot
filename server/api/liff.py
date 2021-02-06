import json

from flask import Blueprint, jsonify, render_template

liff = Blueprint('liff', __name__, url_prefix='/liff')


@liff.route('/', methods=['GET'])
def login():
    return render_template('index.html')


@liff.route('/test', methods=['GET'])
def log():
    return jsonify(name="Chingz")

@liff.route('/logout', methods=['POST'])
def logout():
    return '{"status": "success"} '
