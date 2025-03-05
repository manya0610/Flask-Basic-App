import subprocess
import sys

from sqlalchemy_utils import create_database, database_exists, drop_database

from src.database import engine


def create_db():
    if not database_exists(engine.url):
        print("database doesn't exist, creating it")
        create_database(engine.url)
        print("database created")
    else:
        print("database already exists, dropping it")
        drop_database(engine.url)
        print("database dropped, now creating it")
        create_database(engine.url)
        print("database created")
    engine.dispose()


def drop_db():
    if not database_exists(engine.url):
        print("database doesn't exist")
        raise Exception("database doesn't exist")
    drop_database(engine.url)
    print("database dropped")


def create_tables():
    subprocess.run(["alembic", "upgrade", "head"])


# def create_user():
#     app = create_app()
#     with app.app_context():
#         test_api_org_data = os.getenv("TEST_API_ORG_DATA", None)
#         # create a default user according to env
#         org_name, org_id, api_key = test_api_org_data.split(":")
#         new_org = Org(org_id, org_name, api_key=api_key)
#         db.session.add(new_org)
#         try:
#             db.session.commit()
#         except Exception as e:
#             print("exception while creating org")
#             print(traceback.format_exc())
#             return
#         print("org created")
#         test_api_user_data = os.getenv("TEST_API_USER_DATA", None)
#         account_id, user_name, email, password, role = test_api_user_data.split(":")
#         new_user = User(
#             account_id,
#             new_org.org_id,
#             user_name,
#             email,
#             generate_password_hash(password, method="sha256"),
#             role,
#         )
#         db.session.add(new_user)

#         try:
#             db.session.commit()
#         except Exception as e:
#             print("exception while creating user")
#             print(traceback.format_exc())
#             return
#         print("user created")

print("argument list", sys.argv)

for arg in sys.argv[1:]:
    if arg == "create_db":
        create_db()
    elif arg == "drop_db":
        drop_db()
    elif arg == "create_tables":
        create_tables()
    # elif arg == "create_user":
    #     create_user()
    else:
        print("invalid arg", arg)
