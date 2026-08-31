
import time
import uuid

class Session:
    def __init__(self, user_id):
        self.session_id = str(uuid.uuid4())
        self.user_id = user_id
        self.creation_time = time.time()
        self.last_activity = self.creation_time

class SessionManager:
    def __init__(self, session_timeout=1800):  # Default timeout: 30 minutes
        self.sessions = {}
        self.session_timeout = session_timeout

    def create_session(self, user_id):
        session = Session(user_id)
        self.sessions[session.session_id] = session
        return session.session_id

    def get_session(self, session_id):
        session = self.sessions.get(session_id)
        if session:
            if time.time() - session.last_activity > self.session_timeout:
                self.destroy_session(session_id)
                return None
            session.last_activity = time.time()
        return session

    def destroy_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]

    def cleanup_expired_sessions(self):
        current_time = time.time()
        expired_sessions = [sid for sid, session in self.sessions.items()
                            if current_time - session.last_activity > self.session_timeout]
        for sid in expired_sessions:
            self.destroy_session(sid)

def main():
    session_manager = SessionManager()

    # Create a session
    user_id = "user123"
    session_id = session_manager.create_session(user_id)
    print(f"Session created for user {user_id}: {session_id}")

    # Get session
    session = session_manager.get_session(session_id)
    if session:
        print(f"Session found for user {session.user_id}")
    else:
        print("Session not found")

    # Simulate session expiration
    time.sleep(2)
    session_manager.session_timeout = 1  # Set timeout to 1 second for demonstration
    session = session_manager.get_session(session_id)
    if session:
        print(f"Session still active for user {session.user_id}")
    else:
        print("Session expired")

    # Cleanup expired sessions
    session_manager.cleanup_expired_sessions()
    print("Expired sessions cleaned up")






class TestSessionManager:
    def setUp(self):
        self.session_manager = SessionManager()

    def test_create_session_valid_user_id(self):
        """Test session creation with valid user_id."""
        user_id = "user123"
        session_id = self.session_manager.create_session(user_id)
        assert session_id in self.session_manager.sessions
        assert self.session_manager.sessions[session_id].user_id == user_id

    def test_create_session_unique_session_id(self):
        """Test that session IDs are unique."""
        user_id = "user123"
        session_id1 = self.session_manager.create_session(user_id)
        session_id2 = self.session_manager.create_session(user_id)
        assert session_id1 != session_id2

    def test_get_session_valid_session(self):
        """Test retrieving a valid session."""
        user_id = "user123"
        session_id = self.session_manager.create_session(user_id)
        session = self.session_manager.get_session(session_id)
        assert session is not None
        assert session.user_id == user_id

    def test_get_session_expired(self):
        """Test retrieving an expired session."""
        user_id = "user123"
        session_id = self.session_manager.create_session(user_id)
        time.sleep(2)  # Simulate time passage
        self.session_manager.session_timeout = 1  # Set timeout to 1 second
        session = self.session_manager.get_session(session_id)
        assert session is None

    def test_destroy_session(self):
        """Test destroying a session."""
        user_id = "user123"
        session_id = self.session_manager.create_session(user_id)
        self.session_manager.destroy_session(session_id)
        assert session_id not in self.session_manager.sessions

    def test_destroy_nonexistent_session(self):
        """Test destroying a nonexistent session."""
        non_existent_session_id = str(uuid.uuid4())
        self.session_manager.destroy_session(non_existent_session_id)
        assert non_existent_session_id not in self.session_manager.sessions

    def test_cleanup_expired_sessions(self):
        """Test cleanup of expired sessions."""
        user_id1 = "user123"
        user_id2 = "user456"
        session_id1 = self.session_manager.create_session(user_id1)
        session_id2 = self.session_manager.create_session(user_id2)
        time.sleep(2)  # Simulate time passage
        self.session_manager.session_timeout = 1  # Set timeout to 1 second
        self.session_manager.cleanup_expired_sessions()
        assert session_id1 not in self.session_manager.sessions
        assert session_id2 not in self.session_manager.sessions

    def test_get_session_updates_last_activity(self):
        """Test that retrieving a session updates the last activity time."""
        user_id = "user123"
        session_id = self.session_manager.create_session(user_id)
        initial_last_activity = self.session_manager.get_session(session_id).last_activity
        time.sleep(1)
        self.session_manager.get_session(session_id)
        updated_last_activity = self.session_manager.get_session(session_id).last_activity
        assert updated_last_activity > initial_last_activity

    def test_create_session_session_id_format(self):
        """Test that the session ID format is a valid UUID."""
        user_id = "user123"
        session_id = self.session_manager.create_session(user_id)
        assert isinstance(uuid.UUID(session_id), uuid.UUID)

    def test_no_sessions_after_cleanup(self):
        """Test that all sessions are removed after timeout and cleanup."""
        user_id = "user123"
        session_id = self.session_manager.create_session(user_id)
        time.sleep(2)
        self.session_manager.session_timeout = 1  # Set timeout to 1 second
        self.session_manager.cleanup_expired_sessions()
        assert len(self.session_manager.sessions) == 0



print("All tests passed.")


# Running the tests
test_manager = TestSessionManager()
test_manager.setUp()

# Run each test
test_manager.test_create_session_valid_user_id()
test_manager.test_create_session_unique_session_id()
test_manager.test_get_session_valid_session()
test_manager.test_get_session_expired()
test_manager.test_destroy_session()
test_manager.test_destroy_nonexistent_session()
test_manager.test_cleanup_expired_sessions()
test_manager.test_get_session_updates_last_activity()
test_manager.test_create_session_session_id_format()
test_manager.test_no_sessions_after_cleanup()