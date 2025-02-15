from flask import Flask
from celery import Celery

celery_app = Celery()
celery_app.config_from_object("configs.celeryconfig")


def create_app():
    app = Flask(__name__)
    from src.routes.api_routes import api

    with app.app_context():
        app.register_blueprint(api)

    return app
