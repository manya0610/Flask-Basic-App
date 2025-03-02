from src.database.users import (
    create_user,
    delete_user,
    get_user,
    list_users,
    update_user,
)


# Test for create_user function
def test_create_user_success():
    """Test the success case for create_user."""
    user = create_user("John Doe", "john.doe@example.com")
    
    assert user is not None
    assert user.name == "John Doe"
    assert user.email == "john.doe@example.com"

def test_create_user_failure():
    """Test the failure case for create_user (e.g., duplicate email or invalid input)."""
    # Let's assume there's a unique constraint on email
    create_user("John Doe", "john.doe@example.com")
    user = create_user("Jane Doe", "john.doe@example.com")  # Duplicate email
    
    assert user is None


# Test for get_user function
def test_get_user_found():
    """Test the case where a user is found with get_user."""
    created_user = create_user("John Doe", "john.doe@example.com")
    
    user = get_user(created_user.id)
    
    assert user is not None
    assert user.id == created_user.id
    assert user.name == created_user.name

def test_get_user_not_found():
    """Test the case where no user is found."""
    user = get_user(999)
    
    assert user is None




# Test for list_users function
def test_list_users_success():
    """Test the success case for list_users."""
    create_user("John Doe", "john.doe@example.com")
    create_user("Jane Doe", "jane.doe@example.com")
    
    users = list_users()
    
    assert len(users) >= 2  # Assuming that at least two users are created
    assert any(user.name == "John Doe" for user in users)
    assert any(user.name == "Jane Doe" for user in users)

def test_list_users_empty():
    """Test the case when there are no users."""
    users = list_users()
    
    assert len(users) == 0


# Test for update_user function
def test_update_user_success():
    """Test the success case for update_user."""
    created_user = create_user("John Doe", "john.doe@example.com")
    
    updated_user = update_user(created_user.id, name="Updated Name", email="updated@example.com")
    
    assert updated_user is not None
    assert updated_user.name == "Updated Name"
    assert updated_user.email == "updated@example.com"

def test_update_user_no_changes():
    """Test the case where no fields are provided to update_user."""
    created_user = create_user("John Doe", "john.doe@example.com")
    
    user = update_user(created_user.id)  # No name or email provided
    
    assert user is None

def test_update_user_failure():
    """Test the case where an exception occurs during update_user."""
    _created_user = create_user("John Doe", "john.doe@example.com")
    
    # Simulate failure (e.g., non-existent user ID)
    user = update_user(999, name="Non-Existent", email="nonexistent@example.com")
    
    assert user is None


# Test for delete_user function
def test_delete_user_success():
    """Test the success case for delete_user."""
    created_user = create_user("John Doe", "john.doe@example.com")
    
    success, rowcount = delete_user(created_user.id)
    
    assert success is True
    assert rowcount == 1

def test_delete_user_not_found():
    """Test the case where no user is found to delete."""
    success, rowcount = delete_user(999)
    
    assert success is False
    assert rowcount == 0

def test_delete_user_failure():
    """Test the case where an exception occurs during delete_user."""
    # Simulate a failure by deleting a user that doesn't exist
    success, rowcount = delete_user(999)
    
    assert success is False
    assert rowcount == 0
