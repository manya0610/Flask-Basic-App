from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    from src.routes.api_routes import api

    with app.app_context():
        app.register_blueprint(api)

    return app
