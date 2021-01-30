from flask import Flask
from flask_sqlalchemy import SQLAlchemy

_connection = None

def setConnection(app):
    global _connection
    if not _connection:
        _connection = SQLAlchemy(app)
    return _connection

def getConnection():
    global _connection
    return _connection
        