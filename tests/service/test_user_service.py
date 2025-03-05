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
    email = "john@example.com"

    # Act
    user = create_user(name, email)

    # Assert
    assert user is not None
    assert user.name == name
    assert user.email == email


def test_create_user_duplicate_email():
    # Arrange
    name = "John Doe"
    email = "john@example.com"

    # Create the first user
    create_user(name, email)

    # Act: Try to create another user with the same email
    user = create_user("Jane Doe", email)

    # Assert
    assert user is None  # Assuming duplicate email should return None


# Test Case for `get_user`
def test_get_user_success():
    # Arrange: Create a user
    user = create_user("John Doe", "john@example.com")

    # Act: Retrieve the user by ID
    retrieved_user = get_user(user.id)

    # Assert
    assert retrieved_user is not None
    assert retrieved_user.id == user.id
    assert retrieved_user.name == "John Doe"
    assert retrieved_user.email == "john@example.com"


def test_get_user_not_found():
    # Act: Attempt to retrieve a non-existent user
    retrieved_user = get_user(999)

    # Assert
    assert retrieved_user is None


# Test Case for `list_users`
def test_list_users():
    # Arrange: Create two users
    create_user("John Doe", "john@example.com")
    create_user("Jane Doe", "jane@example.com")

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
    user = create_user("John Doe", "john@example.com")

    # Act: Update the user's name
    updated_user = update_user(user.id, name="Updated Name")

    # Assert
    assert updated_user is not None
    assert updated_user.name == "Updated Name"
    assert updated_user.email == "john@example.com"


def test_update_user_email():
    # Arrange: Create a user
    user = create_user("John Doe", "john@example.com")

    # Act: Update the user's email
    updated_user = update_user(user.id, email="updated@example.com")

    # Assert
    assert updated_user is not None
    assert updated_user.name == "John Doe"
    assert updated_user.email == "updated@example.com"


def test_update_user_not_found():
    # Act: Try updating a non-existent user
    updated_user = update_user(999, name="Updated Name")

    # Assert
    assert updated_user is None


# Test Case for `delete_user`
def test_delete_user_success():
    # Arrange: Create a user
    user = create_user("John Doe", "john@example.com")

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
