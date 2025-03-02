from flask import Blueprint, jsonify, request

from src.database.models import User
from src.service import user_service
from src.validations.user.user_validation import validate_user

api = Blueprint("api", __name__)

# @api.route('/api/hello', methods=['GET'])
# def hello():
#     celery_app.send_task("celery_app.tasks.add", args=[{"message": "boom"}])
#     return jsonify(message="Hello, World!")


@api.route("/api/user", methods=["POST"])
def create_user():
    request_json: dict = request.get_json(silent=True)
    if request_json is None:
        return jsonify({"message": "BAD REQUEST"}), 400

    valid, user_schema = validate_user(request_json)
    if not valid:
        return jsonify({"message": "BAD REQUEST", "error": user_schema}), 400

    name: str = request_json.get("name")
    email: str = request_json.get("email")

    user = user_service.create_user(name, email)
    return jsonify({"user": user.to_dict()})


@api.route("/api/user", methods=["GET"])
def list_users():
    return jsonify({"users": [user.to_dict() for user in user_service.list_users()]})


@api.route("/api/user/<int:id>", methods=["GET"])
def get_user(id: int):
    user: User = user_service.get_user(id)
    if user is None:
        return jsonify({"message": "NOT FOUND"}), 404
    return jsonify({"user": user.to_dict()})


@api.route("/api/user/<int:id>", methods=["PATCH"])
def update_user(id: int):
    request_json: dict = request.get_json(silent=True)
    if request_json is None:
        return jsonify({"message": "BAD REQUEST"}), 400

    user: User = user_service.get_user(id)
    if user is None:
        return jsonify({"message": "NOT FOUND"}), 404

    name: str = request_json.get("name")
    email: str = request_json.get("email")

    user: User = user_service.update_user(id, name, email)
    return jsonify({"user": user.to_dict()})


@api.route("/api/user/<int:id>", methods=["DELETE"])
def delete_user(id: int):
    user: User = user_service.get_user(id)
    if user is None:
        return jsonify({"message": "NOT FOUND"}), 404
    status, message = user_service.delete_user(id)
    if not status:
        return jsonify({"message": message}), 500
    return 210
