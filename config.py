import os
from dotenv import load_dotenv

# Check mode
mode = os.environ.get('MODE')

class Config:
    if mode == 'PROD':
        # Load config vars in Cloud server
        
        # Base flask
        DEBUG = os.environ.get('DEBUG')
        HOST = os.environ.get('HOST')
        PORT = os.environ.get('PORT')
        
        # DB
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
        SQLALCHEMY_TRACK_MODIFICATIONS = os.environment.get('SQLALCHEMY_TRACK_MODIFICATIONS')

        # Line bot
        LINE_CHANNEL_SECRET = os.environ.get('LINE_CHANNEL_SECRET')
        LINE_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
        
    else:
        # Load .env config file
        load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.dev.env'))

        # Base flask
        DEBUG = os.getenv('DEBUG')
        HOST = os.getenv('HOST')
        PORT = os.getenv('PORT')
        
        # DB
        SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
        SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

        # Line bot
        LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
        LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
