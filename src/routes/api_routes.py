from typing import Any, Literal

from flask import Blueprint, Response, jsonify, request

from src.database.models import User
from src.service import user_service
from src.validations.user.user_validation import validate_user, validate_user_update

api = Blueprint("api", __name__)


@api.route("/api/user", methods=["POST"])
def create_user() -> tuple[Response, Literal[200, 400, 404, 500]]:
    request_json: dict[Any, Any] | None = request.get_json(silent=True)
    if request_json is None:
        return jsonify({"message": "BAD REQUEST"}), 400

    valid, user_schema = validate_user(request_json)
    if not valid:
        return jsonify({"message": "BAD REQUEST", "error": user_schema}), 400

    name: str = user_schema.name
    email: str = user_schema.email
    password: str = user_schema.password
    roles: list[str] = user_schema.roles

    user: User | None = user_service.create_user(name, email, password, roles)
    if user is None:
        return jsonify({"message": "INTERNAL SERVER ERROR"}), 500
    return jsonify({"user": user.to_dict()}), 200


@api.route("/api/user", methods=["GET"])
def list_users() -> tuple[Response, Literal[200]]:
    return jsonify(
        {"users": [user.to_dict() for user in user_service.list_users()]}
    ), 200


@api.route("/api/user/<int:id>", methods=["GET"])
def get_user(id: int) -> tuple[Response, Literal[200, 400, 404, 500]]:
    user: User | None = user_service.get_user(id)
    if user is None:
        return jsonify({"message": "NOT FOUND"}), 404
    return jsonify({"user": user.to_dict()}), 200


@api.route("/api/user/<int:id>", methods=["PATCH"])
def update_user(id: int) -> tuple[Response, Literal[200, 400, 404, 500]]:
    request_json: dict[str, Any] | None = request.get_json(silent=True)

    if request_json is None:
        return jsonify({"message": "BAD REQUEST"}), 400

    valid, user_schema = validate_user_update(request_json)
    if not valid:
        return jsonify({"message": "BAD REQUEST", "error": user_schema}), 400

    user: User | None = user_service.get_user(id)
    if user is None:
        return jsonify({"message": "NOT FOUND"}), 404

    name: str = user_schema.name
    email: str = user_schema.email
    password: str = user_schema.password
    roles: list[str] = user_schema.roles

    user = user_service.update_user(id, name, email, password, roles)

    if user is None:
        return jsonify({"message": "INTERNAL SERVER ERROR"}), 500

    return jsonify({"user": user.to_dict()}), 200


@api.route("/api/user/<int:id>", methods=["DELETE"])
def delete_user(id: int) -> tuple[Response, Literal[210, 404, 500]]:
    user: User | None = user_service.get_user(id)
    if user is None:
        return jsonify({"message": "NOT FOUND"}), 404
    status, message = user_service.delete_user(id)
    if not status:
        return jsonify({"message": message}), 500
    return jsonify({"message": "Deleted"}), 210
