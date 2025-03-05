import pytest
from sqlalchemy import MetaData, text
from sqlalchemy.orm import sessionmaker

from src.database import (
    Base,
    db_session,
    engine,
)  # Adjust imports according to your structure

# Ensure Base and db_session are imported correctly in your tests
# Assuming SQLALCHEMY_DATABASE_URL is set correctly in the env file


@pytest.fixture(scope="session")
def init_db():
    """Create tables at the beginning of the test session"""
    # Create all tables in the database
    print("Creating Tables")
    Base.metadata.create_all(bind=engine)
    print("Tables Tables")
    yield
    # After tests, drop the tables (clean up)
    print("Dropping tables")
    Base.metadata.drop_all(bind=engine)
    print("Dropped tables")


@pytest.fixture(scope="function")
def test_db_session(init_db):
    """Set up a session for each test"""
    # Create a scoped session for each test
    Session = sessionmaker(bind=engine)
    session = Session()

    # Bind the session to the db_session object
    db_session.remove()  # Remove any existing session
    db_session.configure(bind=engine)

    # Start a new transaction
    session.begin()
    db_session.session = session
    print("Session created")
    yield session
    # Rollback the transaction to leave no changes in the database
    print("Session rollbacked")
    session.rollback()


@pytest.fixture(scope="function", autouse=True)
def truncate_tables(test_db_session):
    """Truncate all tables before and after each test"""
    metadata = MetaData()
    metadata.reflect(bind=engine)  # Reflect the schema to get all table names
    print("Truncating tables")
    # Truncate all tables
    table_names = [table.name for table in metadata.tables.values()]
    for table_name in table_names:
        truncate_sql = f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE"
        test_db_session.execute(text(truncate_sql))  # Execute truncate SQL

    # Commit the changes
    test_db_session.commit()
