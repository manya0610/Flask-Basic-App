from typing import List, Optional, Tuple

from src.database import user_repo
from src.database.models import User


# Create a user
def create_user(name: str, email: str) -> Optional[User]:
    return user_repo.create_user(name, email)


# Get a user by ID
def get_user(id: int) -> Optional[User]:
    return user_repo.get_user(id)


# List all users
def list_users() -> List[User]:
    return user_repo.list_users()


# Update a user
def update_user(
    id: int, name: Optional[str] = None, email: Optional[str] = None
) -> Optional[User]:
    return user_repo.update_user(id, name, email)


# Delete a user
def delete_user(id: int) -> Tuple[bool, int]:
    return user_repo.delete_user(id)
