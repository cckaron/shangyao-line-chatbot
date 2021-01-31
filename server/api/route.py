from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/user/login', methods=['POST'])
def login():
    return '{"name": "Aaron Kao", "token": "mytoken", "avatar": ' \
           '"https://lh3.googleusercontent.com/ogw/ADGmqu9WYCgH_k7sX1JPJHN7RddvsK6hLEcSCnOWmoTDUsE=s192-c-mo"} '
