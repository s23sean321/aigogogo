import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS =False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='postgresql://s23sean321:pdKVrYpBstM7Eu7NkMyCBhKntRaPlgwH@dpg-cjiu1or37aks73cr6cd0-a.singapore-postgres.render.com/aigogogosql'

class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
