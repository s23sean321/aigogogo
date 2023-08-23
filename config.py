import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS =False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='postgresql://s23sean321:VvsjgLBxas5IBljL5iHwfRE2BHnsP7Vr@dpg-cjig7t0cfp5c73fmnhf0-a.singapore-postgres.render.com/aigosql'

class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
