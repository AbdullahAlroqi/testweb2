import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cofflow-secret-key-2024'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///cofflow.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEFAULT_CUPS_REQUIRED = 6
    
    # إعدادات الجلسة - تبقى لمدة 30 يوم
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)
    SESSION_COOKIE_SECURE = False  # True في الإنتاج مع HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    REMEMBER_COOKIE_DURATION = timedelta(days=30)
    REMEMBER_COOKIE_SECURE = False  # True في الإنتاج مع HTTPS
    REMEMBER_COOKIE_HTTPONLY = True
