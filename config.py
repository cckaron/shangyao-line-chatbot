import os
from dotenv import load_dotenv

isOnHeroku = False
# Check whether it's in heroku env
if os.environ.get('CLEARDB_DATABASE_URL') != None:
    isOnHeroku = True
else:
    # load .env config
    project_folder = os.path.dirname(os.path.abspath(__file__))
    load_dotenv(os.path.join(project_folder, '.dev.env'))

class Config:
    if isOnHeroku:
        #Base flask
        DEBUG = os.environ.get('DEBUG')
        HOST = os.environ.get('HOST')
        PORT = os.environ.get('PORT')
        
        #DB
        DB_SERVER = os.environ.get('CLEARDB_DATABASE_URL')
        DB_PORT = os.environ.get('CLEARDB_DATABASE_URL')
        DB_NAME = os.environ.get('CLEARDB_DATABASE_NAME')
        DB_USER = os.environ.get('CLEARDB_DATABASE_USER')
        DB_PASSWORD = os.environ.get('CLEARDB_DATABASE_PASSWORD')

        #line bot
        LINE_CHANNEL_SECRET = os.environ.get('LINE_CHANNEL_SECRET')
        LINE_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
    else:
        #Base flask
        DEBUG = os.getenv('DEBUG')
        HOST = os.getenv('HOST')
        PORT = os.getenv('PORT')
        
        #DB
        DB_SERVER = os.getenv('DB_SERVER')
        DB_PORT = os.getenv('DB_PORT')
        DB_NAME = os.getenv('DB_NAME')
        DB_USER = os.getenv('DB_USER')
        DB_PASSWORD = os.getenv('DB_PASSWORD')

        #line bot
        LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
        LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
