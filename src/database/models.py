from typing import Any

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY

from src.database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(100))
    roles = Column(ARRAY(String(100)))

    def __init__(self, name: str, email: str, password: str, roles: list) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.roles = roles

    def __repr__(self) -> str:
        return f"<User {self.name!r}>"

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "roles": self.roles,
        }
