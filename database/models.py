from sqlalchemy import Column, Integer, String
from database import Base, metadata

class TestUser(Base):
    __tablename__ = 'test_users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'