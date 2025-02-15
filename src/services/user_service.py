from typing import Tuple
from src.database import db_session
from src.database.models import User

from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import NoResultFound

import logging

logger = logging.getLogger("user_service")


def create_user(name: str, email: str) -> User:
    query = insert(User).values(name=name, email=email).returning(User)
    response: User = db_session.scalar(query)
    db_session.commit()
    return response


def get_user(id: int) -> User:
    try:
        query = select(User).where(User.id == id)
        response: User = db_session.scalars(query).one()
        return response
    except NoResultFound:
        logger.exception("user with id = %d not found", id)
    except Exception:
        logger.exception("Exception while getting user with id = %d", id)
    return None


def list_users() -> list[User]:
    query = select(User)
    response: list[User] = db_session.scalars(query).all()
    return response


def update_user(id: int, name: str = None, email: str = None) -> User:
    values = {"name": name, "email": email}
    values = {key: value for key, value in values.items() if value is not None}
    query = update(User).where(User.id == id).values(values).returning(User)
    response = db_session.scalar(query)
    db_session.commit()
    return response


def delete_user(id: int) -> Tuple[bool, int]:
    query = delete(User).where(User.id == id)
    response = db_session.execute(query)
    db_session.commit()
    return True, response.rowcount
