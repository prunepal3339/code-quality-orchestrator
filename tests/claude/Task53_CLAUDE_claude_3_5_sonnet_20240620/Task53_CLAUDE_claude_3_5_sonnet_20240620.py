import unittest
import time
import uuid
from output.claude.Task53_CLAUDE_claude_3_5_sonnet_20240620 import *

# Assuming the Session and SessionManager classes are already defined above

class TestSessionManager(unittest.TestCase):
    def setUp(self):
        self.session_manager = SessionManager()
        self.user_id = "user123"
        self.session_id = self.session_manager.create_session(self.user_id)

    def test_create_session(self):
        self.assertTrue(self.session_id)
        self.assertIn(self.session_id, self.session_manager.sessions)
        session = self.session_manager.sessions[self.session_id]
        self.assertEqual(session.user_id, self.user_id)
        self.assertIsInstance(session.session_id, str)

    def test_get_session(self):
        session = self.session_manager.get_session(self.session_id)
        self.assertIsNotNone(session)
        self.assertEqual(session.user_id, self.user_id)

    def test_get_invalid_session(self):
        invalid_session_id = str(uuid.uuid4())
        session = self.session_manager.get_session(invalid_session_id)
        self.assertIsNone(session)

    def test_session_timeout(self):
        self.session_manager.session_timeout = 1  # Set a short timeout for testing
        time.sleep(2)  # Wait for the session to expire
        session = self.session_manager.get_session(self.session_id)
        self.assertIsNone(session)

    def test_destroy_session(self):
        self.session_manager.destroy_session(self.session_id)
        self.assertNotIn(self.session_id, self.session_manager.sessions)

    def test_cleanup_expired_sessions(self):
        self.session_manager.session_timeout = 1  # Set a short timeout for testing
        session_id2 = self.session_manager.create_session("user456")
        time.sleep(2)  # Wait for the first session to expire
        self.session_manager.cleanup_expired_sessions()
        self.assertNotIn(self.session_id, self.session_manager.sessions)
        self.assertIn(session_id2, self.session_manager.sessions)

    def test_cleanup_no_expired_sessions(self):
        session_id2 = self.session_manager.create_session("user789")
        self.session_manager.cleanup_expired_sessions()
        self.assertIn(self.session_id, self.session_manager.sessions)
        self.assertIn(session_id2, self.session_manager.sessions)

    def test_update_last_accessed(self):
        time.sleep(1)
        session = self.session_manager.get_session(self.session_id)
        self.assertIsNotNone(session)
        self.assertGreater(session.last_accessed, session.created_at)

    def test_create_multiple_sessions(self):
        session_id2 = self.session_manager.create_session("user456")
        self.assertIn(session_id2, self.session_manager.sessions)
        self.assertNotEqual(self.session_id, session_id2)

    def test_destroy_non_existent_session(self):
        non_existent_session_id = str(uuid.uuid4())
        self.session_manager.destroy_session(non_existent_session_id)
        self.assertNotIn(non_existent_session_id, self.session_manager.sessions)

if __name__ == "__main__":
    unittest.main()