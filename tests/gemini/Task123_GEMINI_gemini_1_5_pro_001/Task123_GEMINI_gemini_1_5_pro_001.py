import datetime

class Session:
  def __init__(self, username):
    self.username = username
    self.session_id = None
    self.created_at = datetime.datetime.now()

  def create_session(self):
    # In a real application, generate a unique session ID
    self.session_id = "session_" + self.username

  def is_valid(self):
    # In a real application, check for session expiry
    return True

class SessionManager:
  def __init__(self):
    self.sessions = {}

  def create_session(self, username):
    session = Session(username)
    session.create_session()
    self.sessions[session.session_id] = session
    return session.session_id

  def get_session(self, session_id):
    return self.sessions.get(session_id)

  def delete_session(self, session_id):
    if session_id in self.sessions:
      del self.sessions[session_id]



class TestSessionManager:
  def setUp(self):
    self.session_manager = SessionManager()

  def test_create_session_valid_username(self):
    """Test session creation with a valid username."""
    username = "user123"
    session_id = self.session_manager.create_session(username)
    session = self.session_manager.get_session(session_id)
    
    assert session is not None
    assert session.username == username

  def test_create_session_unique_session_id(self):
    """Test that session IDs are unique."""
    username1 = "user123"
    username2 = "user456"
    session_id1 = self.session_manager.create_session(username1)
    session_id2 = self.session_manager.create_session(username2)
    assert session_id1 != session_id2

  def test_session_id_format(self):
    """Test that the session ID format is correct."""
    username = "user123"
    session_id = self.session_manager.create_session(username)
    assert session_id == "session_" + username

  def test_get_session_valid_session(self):
    """Test retrieving a valid session."""
    username = "user123"
    session_id = self.session_manager.create_session(username)
    session = self.session_manager.get_session(session_id)
    assert session is not None
    assert session.username == username

  def test_get_session_non_existent(self):
    """Test retrieving a non-existent session."""
    session = self.session_manager.get_session("non_existent_session")
    assert session is None

  def test_delete_session(self):
    """Test deleting a session."""
    username = "user123"
    session_id = self.session_manager.create_session(username)
    self.session_manager.delete_session(session_id)
    assert self.session_manager.get_session(session_id) is None

  def test_delete_non_existent_session(self):
    """Test deleting a non-existent session."""
    initial_sessions_count = len(self.session_manager.sessions)
    self.session_manager.delete_session("non_existent_session")
    assert len(self.session_manager.sessions) == initial_sessions_count

  def test_session_created_at(self):
    """Test that the session's created_at is set correctly."""
    username = "user123"
    session_id = self.session_manager.create_session(username)
    session = self.session_manager.get_session(session_id)
    assert session.created_at is not None
    assert isinstance(session.created_at, datetime.datetime)

  def test_session_is_valid(self):
    """Test that session is considered valid."""
    username = "user123"
    session_id = self.session_manager.create_session(username)
    session = self.session_manager.get_session(session_id)
    assert session.is_valid() is True

  def test_create_multiple_sessions(self):
    """Test creating multiple sessions for different usernames."""
    username1 = "user123"
    username2 = "user456"
    session_id1 = self.session_manager.create_session(username1)
    session_id2 = self.session_manager.create_session(username2)
    assert self.session_manager.get_session(session_id1) is not None
    assert self.session_manager.get_session(session_id2) is not None
    assert session_id1 != session_id2




if __name__ == "__main__":

  test_manager = TestSessionManager()
  test_manager.setUp()
  
  # Run each test
  test_manager.test_create_session_valid_username()
  test_manager.test_create_session_unique_session_id()
  test_manager.test_session_id_format()
  test_manager.test_get_session_valid_session()
  test_manager.test_get_session_non_existent()
  test_manager.test_delete_session()
  test_manager.test_delete_non_existent_session()
  test_manager.test_session_created_at()
  test_manager.test_session_is_valid()
  test_manager.test_create_multiple_sessions()
  print("All tests Done.")
  
