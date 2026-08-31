import unittest

class Session:
    def __init__(self, user_id):
        self.user_id = user_id
        self.is_active = True

class TestSession(unittest.TestCase):
    def setUp(self):
        self.user_id = "123"
        self.session = Session(self.user_id)

    def test_session_creation(self):
        # Test if the session is created with the correct user_id
        self.assertEqual(self.session.user_id, self.user_id)
        self.assertTrue(self.session.is_active)

    def test_session_initial_state(self):
        # Test if the session starts as active
        self.assertTrue(self.session.is_active)

    def test_user_sessions_storage(self):
        # Test if the session is stored correctly in the user_sessions dictionary
        user_sessions = {}
        user_sessions[self.user_id] = self.session
        self.assertIn(self.user_id, user_sessions)
        self.assertIs(user_sessions[self.user_id], self.session)

    def test_session_inactive(self):
        # Set the session to inactive and test
        self.session.is_active = False
        self.assertFalse(self.session.is_active)

if __name__ == "__main__":
    unittest.main()