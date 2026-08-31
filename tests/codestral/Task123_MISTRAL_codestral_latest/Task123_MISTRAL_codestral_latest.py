# Python
class Session:
    def __init__(self, user_id):
        self.user_id = user_id
        self.is_active = True

    def end_session(self):
        self.is_active = False

class TestSession:
    def test_session_creation_valid_user_id(self):
        """Test session creation with a valid user ID."""
        user_id = "user123"
        session = Session(user_id)
        assert session.user_id == user_id
        assert session.is_active is True

    def test_session_initial_state_is_active(self):
        """Test that a session is active upon creation."""
        session = Session("user123")
        assert session.is_active is True

    def test_end_session_changes_is_active(self):
        """Test that ending the session sets is_active to False."""
        session = Session("user123")
        session.end_session()
        assert session.is_active is False

    def test_end_session_called_once(self):
        """Test that calling end_session once deactivates the session."""
        session = Session("user123")
        session.end_session()
        assert session.is_active is False

    def test_end_session_called_multiple_times(self):
        """Test that calling end_session multiple times doesn't change the state after the first call."""
        session = Session("user123")
        session.end_session()
        session.end_session()
        assert session.is_active is False

    def test_session_creation_with_different_user_ids(self):
        """Test session creation with different user IDs."""
        session1 = Session("user123")
        session2 = Session("user456")
        assert session1.user_id != session2.user_id
        assert session1.is_active is True
        assert session2.is_active is True

    def test_multiple_sessions_independent(self):
        """Test that multiple sessions are independent of each other."""
        session1 = Session("user123")
        session2 = Session("user456")
        session1.end_session()
        assert session1.is_active is False
        assert session2.is_active is True

    def test_is_active_not_affected_by_external_factors(self):
        """Test that is_active is not modified by external variables."""
        session = Session("user123")
        external_flag = False
        assert session.is_active is True
        assert external_flag is False

    def test_end_session_not_callable_directly(self):
        """Test that end_session is callable and modifies the state."""
        session = Session("user123")
        assert callable(session.end_session) is True
        session.end_session()
        assert session.is_active is False

    def test_user_id_remains_unchanged_after_end_session(self):
        """Test that the user_id remains unchanged after ending the session."""
        user_id = "user123"
        session = Session(user_id)
        session.end_session()
        assert session.user_id == user_id

# Running the tests
test_session = TestSession()

# Run each test
test_session.test_session_creation_valid_user_id()
test_session.test_session_initial_state_is_active()
test_session.test_end_session_changes_is_active()
test_session.test_end_session_called_once()
test_session.test_end_session_called_multiple_times()
test_session.test_session_creation_with_different_user_ids()
test_session.test_multiple_sessions_independent()
test_session.test_is_active_not_affected_by_external_factors()
test_session.test_end_session_not_callable_directly()
test_session.test_user_id_remains_unchanged_after_end_session()

print("All tests passed.")
