from typing import Literal, Optional

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    name: str = Field(min_length=4, max_length=100)
    password: str = Field(min_length=8, max_length=100)
    email: EmailStr = Field(max_length=100)
    roles: list[Literal["user", "admin", "superadmin"]]


class UserUpdateSchema(BaseModel):
    name: Optional[str | None] = Field(default=None, min_length=4, max_length=100)
    password: Optional[str | None] = Field(default=None, min_length=8, max_length=100)
    email: Optional[EmailStr | None] = Field(default=None, max_length=100)
    roles: Optional[list[Literal["user", "admin", "superadmin"]] | None] = Field(
        default=None
    )


# PASSWORD_REGEX = r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[\~\!\@\#\$\%\^\&\*\(\)\_\+\`\-\=\{\}\[\]\"\'\:\;\<\>\,\.\?])[^\s]{8,50}$"
# USER_NAME_REGEX = r"^(?! )[A-Za-z0-9@\-# _.]+$"


# class UserSchema(BaseModel):
#     account_id: Union[UUID, None] = Field(default=None)
#     org_id: UUID = Field()
#     user_name: str = Field(min_length=4, max_length=50)
#     email: EmailStr = Field(max_length=100)
#     password: str = Field(min_length=8, max_length=100)
#     role: Literal["USER", "SUPERADMIN"] = Field(default="USER")

#     @field_validator("org_id")
#     @classmethod
#     def validate_org_id(cls, org_id):
#         status, message = OrgService.get_org(org_id)
#         if status:
#             return org_id
#         raise PydanticCustomError(
#             "invalid_org_id",
#             message,
#             {"org_id": org_id},
#         )

#     @field_validator("user_name")
#     @classmethod
#     def validate_user_name(cls, user_name):
#         if re.match(USER_NAME_REGEX, user_name):
#             return user_name

#         raise PydanticCustomError(
#             "invalid_user_name",
#             "user_name should not start with a space, and it can only contain letters, digits, and the special characters @, -, #, space, _, .",
#             {"user_name": user_name},
#         )

#     @field_validator("password")
#     @classmethod
#     def validate_password(cls, password):
#         if re.match(PASSWORD_REGEX, password):
#             return password

#         raise PydanticCustomError(
#             "weak_password",
#             "Password should have minimum length of 8, one lowercase character, one uppercase character, one special character, one number and no whitespaces",
#             {"password": password},
#         )


# class UserUpdateSchema(BaseModel):

#     org_id: Union[UUID, None] = Field(default=None)
#     user_name: Union[str, None] = Field(default=None, min_length=4, max_length=50)
#     email: Union[EmailStr, None] = Field(default=None, max_length=100)
#     password: Union[str, None] = Field(default=None, min_length=8, max_length=100)
#     role: Union[Literal["USER", "SUPERADMIN"], None] = Field(default=None)

#     @field_validator("org_id")
#     @classmethod
#     def validate_org_id(cls, org_id):
#         status, message = OrgService.get_org(org_id)
#         if status:
#             return org_id
#         raise PydanticCustomError(
#             "invalid_org_id",
#             message,
#             {"org_id": org_id},
#         )

#     @field_validator("user_name")
#     @classmethod
#     def validate_user_name(cls, user_name):
#         if re.match(USER_NAME_REGEX, user_name):
#             return user_name

#         raise PydanticCustomError(
#             "invalid_user_name",
#             "user_name should not start with a space, and it can only contain letters, digits, and the special characters @, -, #, space, _, .",
#             {"user_name": user_name},
#         )

#     @field_validator("password")
#     @classmethod
#     def validate_password(cls, password):
#         if re.match(PASSWORD_REGEX, password):
#             return password

#         raise PydanticCustomError(
#             "invalid_password",
#             "Password should have minimum length of 8, one lowercase character, one uppercase character, one special character, one number and no whitespaces",
#             {"password": password},
#         )
