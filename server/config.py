import os

class Config(object):
    DB_SERVER_URL = os.environ.get('DB_SERVER_URL') or 'comb-ai.civtuupr4nks.us-east-2.rds.amazonaws.com'
    DB_NAME     = os.environ.get('DB_NAME') or 'combAI'
    DB_PORT     = os.environ.get('DB_PORT')  or 3306
    DB_USER     = os.environ.get('DB_USER')  or 'admin'
    DB_PASSW    = os.environ.get('DB_PASSW') or 'combineai'

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or f'mysql+pymysql://{DB_USER}:{DB_PASSW}@{DB_SERVER_URL}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
 


    