from typing import Optional

from src.database.models import User
from src.repo import user_repo


# Create a user
def create_user(name: str, email: str, password: str, roles: list[str]) -> User:
    return user_repo.create_user(name, email, password, roles)


# Get a user by ID
def get_user(id: int) -> User:
    return user_repo.get_user(id)


# List all users
def list_users(limit: int = 100, offset: int = 0) -> list[User]:
    return user_repo.list_users(limit, offset)


# Update a user
def update_user(
    id: int,
    name: Optional[str] = None,
    email: Optional[str] = None,
    password: Optional[str] = None,
    roles: Optional[list] = None,
) -> User:
    return user_repo.update_user(id, name, email, password, roles)


# Delete a user
def delete_user(id: int) -> int:
    return user_repo.delete_user(id)
