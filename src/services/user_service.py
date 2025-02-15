from typing import Tuple
from src.database import db_session
from src.database.models import TestUser

from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import NoResultFound

import logging

logger = logging.getLogger("user_service")


def create_user(name: str, email: str) -> TestUser:
    query = insert(TestUser).values(name=name, email=email).returning(TestUser)
    response: TestUser = db_session.scalar(query)
    db_session.commit()
    return response


def get_user(id: int) -> TestUser:
    try:
        query = select(TestUser).where(TestUser.id == id)
        response: TestUser = db_session.scalars(query).one()
        return response
    except NoResultFound:
        logger.exception("user with id = %d not found", id)
    except Exception:
        logger.exception("Exception while getting user with id = %d", id)
    return None


def list_users() -> list[TestUser]:
    query = select(TestUser)
    response: list[TestUser] = db_session.scalars(query).all()
    return response


def update_user(id: int, name: str = None, email: str = None) -> TestUser:
    values = {"name": name, "email": email}
    values = {key: value for key, value in values.items() if value is not None}
    query = update(TestUser).where(TestUser.id == id).values(values).returning(TestUser)
    response = db_session.scalar(query)
    db_session.commit()
    return response


def delete_user(id: int) -> Tuple[bool, int]:
    query = delete(TestUser).where(TestUser.id == id)
    response = db_session.execute(query)
    db_session.commit()
    return True, response.rowcount
