from typing import List, Optional, Tuple

from src.database import users
from src.database.models import User


# Create a user
def create_user(name: str, email: str) -> Optional[User]:
    return users.create_user(name, email)


# Get a user by ID
def get_user(id: int) -> Optional[User]:
    return users.get_user(id)


# List all users
def list_users() -> List[User]:
    return users.list_users()


# Update a user
def update_user(
    id: int, name: Optional[str] = None, email: Optional[str] = None
) -> Optional[User]:
    return users.update_user(id, name, email)


# Delete a user
def delete_user(id: int) -> Tuple[bool, int]:
    return users.delete_user(id)
