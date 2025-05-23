from typing import Literal

from flask import Blueprint, Response, jsonify

from src.celery_app import celery_app
from src.controller.user_controller import user_blueprint

api = Blueprint("api", __name__, url_prefix="/api")

api.register_blueprint(user_blueprint)


@api.route("/test", methods=["POST"])
def test() -> tuple[Response, Literal[200]]:
    celery_app.send_task("src.celery_app.tasks.add", [1])
    return jsonify({"message": "ok"}), 200
