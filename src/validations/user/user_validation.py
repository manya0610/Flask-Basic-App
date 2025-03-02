from pydantic import ValidationError

from src.validations.helper import pydantic_error_parser
from src.validations.user.user_schema import UserSchema


def validate_user(data: dict):
    try:
        user: UserSchema = UserSchema.model_validate(data)
        return True, user
    except ValidationError as e:
        return False, pydantic_error_parser(e.errors())
    except Exception as e:
        print(e)
        return False, {"error": "unknown exception"}


# def validate_user_update(data: dict):
#     try:
#         user = UserUpdateSchema.model_validate(data)
#         return True, user
#     except ValidationError as e:
#         # log_error(None, None, e.errors())
#         return False, pydantic_error_parser(e.errors())
#     except Exception as e:
#         log_error(
#             None, None, "Unknown Exception while validating", print_traceback=True
#         )
#         return False, "unknown exception"
