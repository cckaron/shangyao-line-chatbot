from flask_sqlalchemy import SQLAlchemy

_connection = None


def set_connection(app):
    global _connection
    if not _connection:
        _connection = SQLAlchemy(app)
    return _connection


def get_connection():
    global _connection
    return _connection
