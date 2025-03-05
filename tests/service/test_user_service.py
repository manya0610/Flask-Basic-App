from src.service.user_service import (
    create_user,
    delete_user,
    get_user,
    list_users,
    update_user,
)


# Test Case for `create_user`
def test_create_user_success():
    # Arrange
    name = "John Doe"
    email = "john.doe@example.com"
    password = "123456"
    roles = ["user"]
    user = create_user(name, email, password, roles)

    # Assert
    assert user is not None
    assert user.name == name
    assert user.email == email


def test_create_user_duplicate_email():
    # Arrange
    name = "John Doe"
    email = "john.doe@example.com"
    password = "123456"
    roles = ["user"]

    user = create_user(name, email, password, roles)

    # Act: Try to create another user with the same email
    user = create_user("Jane Doe", email, password, roles)

    # Assert
    assert user is None  # Assuming duplicate email should return None


# Test Case for `get_user`
def test_get_user_success():
    # Arrange: Create a user
    name = "John Doe"
    email = "john.doe@example.com"
    password = "123456"
    roles = ["user"]
    user = create_user(name, email, password, roles)

    # Act: Retrieve the user by ID
    retrieved_user = get_user(user.id)

    # Assert
    assert retrieved_user is not None
    assert retrieved_user.id == user.id
    assert retrieved_user.name == name
    assert retrieved_user.email == email


def test_get_user_not_found():
    # Act: Attempt to retrieve a non-existent user
    retrieved_user = get_user(999)

    # Assert
    assert retrieved_user is None


# Test Case for `list_users`
def test_list_users():
    # Arrange: Create two users
    user1_name = "John Doe"
    user1_email = "john.doe@example.com"
    user1_password = "123456"
    user1_roles = ["user"]

    user2_name = "Jane Doe"
    user2_email = "jane.doe@example.com"
    user2_password = "123456"
    user2_roles = ["user"]
    create_user(user1_name, user1_email, user1_password, user1_roles)
    create_user(user2_name, user2_email, user2_password, user2_roles)

    # Act: List all users
    users_list = list_users()

    # Assert
    assert len(users_list) >= 2  # At least the two users should exist
    assert any(user.name == "John Doe" for user in users_list)
    assert any(user.name == "Jane Doe" for user in users_list)


def test_list_users_empty():
    # Act: List users when the database is empty
    users_list = list_users()

    # Assert
    assert len(users_list) == 0  # No users should be present


# Test Case for `update_user`
def test_update_user_name():
    # Arrange: Create a user
    name = "John Doe"
    email = "john.doe@example.com"
    password = "123456"
    roles = ["user"]
    created_user = create_user(name, email, password, roles)

    # Act: Update the user's name
    updated_user = update_user(created_user.id, name="Updated Name")

    # Assert
    assert updated_user is not None
    assert updated_user.name == "Updated Name"
    assert updated_user.email == email
    assert updated_user.password == password
    assert updated_user.roles == roles


def test_update_user():
    # Arrange: Create a user
    name = "John Doe"
    email = "john.doe@example.com"
    password = "123456"
    roles = ["user"]
    created_user = create_user(name, email, password, roles)

    # Act: Update the user's email
    updated_email = "updated@example.com"
    updated_password = "12345678"
    updated_roles = ["superadmin"]
    updated_user = update_user(
        created_user.id,
        email=updated_email,
        password=updated_password,
        roles=updated_roles,
    )

    # Assert
    assert updated_user is not None
    assert updated_user.name == name
    assert updated_user.email == updated_email
    assert updated_user.password == updated_password
    assert updated_user.roles == updated_roles


def test_update_user_not_found():
    # Act: Try updating a non-existent user
    updated_user = update_user(999, name="Updated Name")

    # Assert
    assert updated_user is None


# Test Case for `delete_user`
def test_delete_user_success():
    # Arrange: Create a user
    name = "John Doe"
    email = "john.doe@example.com"
    password = "123456"
    roles = ["user"]
    user = create_user(name, email, password, roles)

    # Act: Delete the user
    success, user_id = delete_user(user.id)

    # Assert
    assert success is True
    assert user_id == user.id


def test_delete_user_not_found():
    # Act: Try deleting a non-existent user
    success, user_id = delete_user(999)

    # Assert
    assert success is False
    assert user_id == 0
