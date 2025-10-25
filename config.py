import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cofflow-secret-key-2024'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///cofflow.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEFAULT_CUPS_REQUIRED = 6
