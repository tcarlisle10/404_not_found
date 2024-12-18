# import os

# # config.py

# class Config:
#     SECRET_KEY = "your_secret_key"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# class DevelopmentConfig(Config):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:password@localhost/your_db"



# class TextingConfig:
#     pass

# class ProductionConfig:
#     pass
# config.py

class Config:
    SECRET_KEY = "your_secret_key"
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:Migmaster10!@localhost/skill_x_change"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

