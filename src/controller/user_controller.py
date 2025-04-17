from typing import Any, Literal

from flask import Blueprint, Response, jsonify, request

from src.database.models import User
from src.exceptions.db_exceptions import DatabaseError, NotFoundError
from src.exceptions.request_exceptions import BadRequestError, InvalidJSONError
from src.service import user_service
from src.validations.user.user_validation import validate_user, validate_user_update
from src.constants.error_messages import BAD_REQUEST, INTERNAL_SERVER_ERROR, NOT_FOUND

user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.route("", methods=["POST"])
def create_user() -> tuple[Response, Literal[200, 400, 500]]:
    try:
        request_json: dict[Any, Any] | None = request.get_json(silent=True)
        if request_json is None:
            raise InvalidJSONError
        user_schema = validate_user(request_json)
        name: str = user_schema.name
        email: str = user_schema.email
        password: str = user_schema.password
        roles: list[str] = user_schema.roles
        user: User = user_service.create_user(name, email, password, roles)
        return jsonify({"user": user.to_dict()}), 200

    except (InvalidJSONError,  BadRequestError) as e:
        return jsonify({"message": BAD_REQUEST,
                        "error" :  e.error_dict}), 400
    except DatabaseError:
        return jsonify({"message": INTERNAL_SERVER_ERROR}), 500


@user_blueprint.route("", methods=["GET"])
def list_users() -> tuple[Response, Literal[200]]:
    try:
        return jsonify(
            {"users": [user.to_dict() for user in user_service.list_users()]}
        ), 200
    except (InvalidJSONError,  BadRequestError) as e:
        return jsonify({"message": BAD_REQUEST,
                        "error" :  e.error_dict}), 400
    except DatabaseError:
        return jsonify({"message": INTERNAL_SERVER_ERROR}), 500


@user_blueprint.route("/<int:id>", methods=["GET"])
def get_user(id: int) -> tuple[Response, Literal[200, 400, 404, 500]]:
    try:
        user: User = user_service.get_user(id)
        return jsonify({"user": user.to_dict()}), 200
    except NotFoundError:
        return jsonify({"message": NOT_FOUND}), 404
    except (InvalidJSONError,  BadRequestError) as e:
        return jsonify({"message": BAD_REQUEST,
                        "error" :  e.error_dict}), 400
    except DatabaseError:
        return jsonify({"message": INTERNAL_SERVER_ERROR}), 500


@user_blueprint.route("/<int:id>", methods=["PATCH"])
def update_user(id: int) -> tuple[Response, Literal[200, 400, 404, 500]]:
    try:
        request_json: dict[str, Any] | None = request.get_json(silent=True)

        if request_json is None:
            raise InvalidJSONError

        user_schema = validate_user_update(request_json)

        name: str = user_schema.name
        email: str = user_schema.email
        password: str = user_schema.password
        roles: list[str] = user_schema.roles

        user = user_service.update_user(id, name, email, password, roles)

        return jsonify({"user": user.to_dict()}), 200

    except NotFoundError:
        return jsonify({"message": NOT_FOUND}), 404
    except (InvalidJSONError,  BadRequestError) as e:
        return jsonify({"message": BAD_REQUEST,
                        "error" :  e.error_dict}), 400
    except DatabaseError:
        return jsonify({"message": INTERNAL_SERVER_ERROR}), 500


@user_blueprint.route("/<int:id>", methods=["DELETE"])
def delete_user(id: int) -> tuple[Response, Literal[210, 404, 500]]:
    try:
        deleted_row_count = user_service.delete_user(id)

        return jsonify({"message": f"Deleted {deleted_row_count} rows"}), 210
    except NotFoundError:
        return jsonify({"message": NOT_FOUND}), 404
    except (InvalidJSONError,  BadRequestError) as e:
        return jsonify({"message": BAD_REQUEST,
                        "error" :  e.error_dict}), 400
    except DatabaseError:
        return jsonify({"message": INTERNAL_SERVER_ERROR}), 500
