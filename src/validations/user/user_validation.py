from pydantic import ValidationError

from src.exceptions.request_exceptions import BadRequestError
from src.validations.helper import pydantic_error_parser
from src.validations.user.user_schema import UserSchema, UserUpdateSchema


def validate_user(data: dict) -> UserSchema:
    try:
        return UserSchema.model_validate(data)
    except ValidationError as e:
        raise BadRequestError(error_dict=pydantic_error_parser(e.errors())) from e
    except Exception:
        raise


def validate_user_update(data: dict) -> UserSchema:
    try:
        return UserUpdateSchema.model_validate(data)
    except ValidationError as e:
        # log_error(None, None, e.errors())
        raise BadRequestError(error_dict=pydantic_error_parser(e.errors())) from e
    except Exception:
        raise
