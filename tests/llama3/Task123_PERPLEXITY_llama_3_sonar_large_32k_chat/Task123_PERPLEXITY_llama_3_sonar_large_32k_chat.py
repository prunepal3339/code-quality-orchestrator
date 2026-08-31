class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id, username):
        self.sessions[user_id] = username
        print(f"Session created for user {username} with ID {user_id}")
        return [username,user_id]

    def get_username(self, user_id):
        return self.sessions.get(user_id)

    def delete_session(self, user_id):
        if user_id in self.sessions:
            del self.sessions[user_id]
            print(f"Session deleted for user ID {user_id}")
            return [0,user_id]
        else:
            print(f"No session found for user ID {user_id}")
            return [1,user_id]


class TestSessionManager:
    def setUp(self):
        """Initialize SessionManager for testing."""
        self.manager = SessionManager()

    def test_create_session(self):
        """Test creating a session."""
        user_id = "user123"
        username = "john_doe"
        result = self.manager.create_session(user_id, username)
        expected = [username, user_id]
        assert result == expected
        assert self.manager.get_username(user_id) == username

    def test_get_existing_username(self):
        """Test getting username for an existing user ID."""
        user_id = "user456"
        username = "jane_doe"
        self.manager.create_session(user_id, username)
        result = self.manager.get_username(user_id)
        assert result == username

    def test_get_non_existing_username(self):
        """Test getting username for a non-existing user ID."""
        result = self.manager.get_username("non_existing_id")
        assert result is None

    def test_delete_existing_session(self):
        """Test deleting an existing session."""
        user_id = "user789"
        username = "alice"
        self.manager.create_session(user_id, username)
        result = self.manager.delete_session(user_id)
        expected = [0, user_id]
        assert result == expected
        assert self.manager.get_username(user_id) is None

    def test_delete_non_existing_session(self):
        """Test deleting a non-existing session."""
        result = self.manager.delete_session("non_existing_id")
        expected = [1, "non_existing_id"]
        assert result == expected

    def test_session_replacement(self):
        """Test that a session can be replaced."""
        user_id = "user101"
        username1 = "bob"
        username2 = "alice"
        self.manager.create_session(user_id, username1)
        self.manager.create_session(user_id, username2)  # Overwrite the session
        result = self.manager.get_username(user_id)
        assert result == username2

    def test_multiple_sessions(self):
        """Test creating and retrieving multiple sessions."""
        user1_id = "user202"
        user1_name = "charlie"
        user2_id = "user303"
        user2_name = "daisy"
        self.manager.create_session(user1_id, user1_name)
        self.manager.create_session(user2_id, user2_name)
        assert self.manager.get_username(user1_id) == user1_name
        assert self.manager.get_username(user2_id) == user2_name

    def test_session_deletion_output(self):
        """Test the output of session deletion."""
        user_id = "user404"
        username = "eve"
        self.manager.create_session(user_id, username)
        result = self.manager.delete_session(user_id)
        assert result == [0, user_id]

    def test_session_deletion_output_non_existing(self):
        """Test the output of deleting a non-existing session."""
        result = self.manager.delete_session("non_existing_id")
        assert result == [1, "non_existing_id"]

    def test_create_session_multiple_times(self):
        """Test creating the same session multiple times."""
        user_id = "user505"
        username = "frank"
        result1 = self.manager.create_session(user_id, username)
        result2 = self.manager.create_session(user_id, username)  # Should overwrite
        assert result1 == [username, user_id]
        assert result2 == [username, user_id]
        assert self.manager.get_username(user_id) == username

# Running the tests
test_session_manager = TestSessionManager()
test_session_manager.setUp()

# Run each test
test_session_manager.test_create_session()
test_session_manager.test_get_existing_username()
test_session_manager.test_get_non_existing_username()
test_session_manager.test_delete_existing_session()
test_session_manager.test_delete_non_existing_session()
test_session_manager.test_session_replacement()
test_session_manager.test_multiple_sessions()
test_session_manager.test_session_deletion_output()
test_session_manager.test_session_deletion_output_non_existing()
test_session_manager.test_create_session_multiple_times()

print("All tests passed.")