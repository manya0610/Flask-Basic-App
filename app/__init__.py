from flask import Flask
from celery import Celery

celery_app = Celery()
celery_app.config_from_object("configs.celeryconfig")


def create_app():
    app = Flask(__name__)
    
    with app.app_context():
        from .api import api
        app.register_blueprint(api)
    
    return app

