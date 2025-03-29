import logging
from typing import List, Optional, Sequence

from sqlalchemy import delete, insert, select, update

from src.database import db_session
from src.database.models import User
from src.exceptions.db_exceptions import DataBaseError, NotFoundError

logging.basicConfig()
logger = logging.getLogger(__name__)


# Create a user, returning a User object or None
def create_user(name: str, email: str, password: str, roles: list) -> User:
    try:
        query = (
            insert(User)
            .values(name=name, email=email, password=password, roles=roles)
            .returning(User)
        )
        response: Optional[User] = db_session.scalar(query)
        db_session.commit()
        return response
    except Exception as e:
        db_session.rollback()
        logger.exception("Error creating user with email=%s: %s", email, str(e))
        raise DataBaseError from e


# Get a user by ID, returning a User object or None
def get_user(id: int) -> User:
    try:
        query = select(User).where(User.id == id)
        response: Optional[User] = db_session.scalars(query).one_or_none()
        if response is None:
            logger.warning("User with id=%s not found", id)
            raise NotFoundError
        return response
    except NotFoundError:
        raise
    except Exception as e:
        logger.exception("Error while getting user with id=%s: %s", id, str(e))
        raise DataBaseError from e


# List all users, returning a list of User objects
def list_users() -> List[User]:
    try:
        query = select(User)
        response: Sequence[User] = db_session.scalars(query).all()
        return list(response)
    except Exception as e:
        logger.exception("Error while listing users: %s", str(e))
        raise DataBaseError from e


# Update a user, returning the updated User object or None
def update_user(
    id: int,
    name: Optional[str] = None,
    email: Optional[str] = None,
    password: Optional[str] = None,
    roles: Optional[list] = None,
) -> User:
    try:
        values = {"name": name, "email": email, "password": password, "roles": roles}
        values = {key: value for key, value in values.items() if value is not None}

        if not values:
            logger.warning("No fields provided to update for user with id=%d", id)
            return None

        query = update(User).where(User.id == id).values(values).returning(User)
        response: Optional[User] = db_session.scalar(query)
        db_session.commit()
        if response is None:
            logger.warning("No user found with id=%s to update", id)
            raise NotFoundError

        return response
    except NotFoundError:
        raise
    except Exception as e:
        db_session.rollback()
        logger.exception("Error updating user with id=%s: %s", id, str(e))
        raise DataBaseError from e


# Delete a user by ID, returning a tuple (bool, int) indicating success and row count
def delete_user(id: int) -> int:
    try:
        query = delete(User).where(User.id == id)
        response = db_session.execute(query)
        db_session.commit()

        if response.rowcount == 0:
            logger.warning("No user found with id=%s to delete", id)
            raise NotFoundError

        return response.rowcount
    except NotFoundError:
        raise
    except Exception as e:
        db_session.rollback()
        logger.exception("Error deleting user with id=%s: %s", id, str(e))
        raise DataBaseError from e
