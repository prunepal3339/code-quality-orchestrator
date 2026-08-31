import time

class UserSession:
    def __init__(self, user_id):
        self.user_id = user_id
        self.start_time = time.time()

    def get_duration(self):
        return time.time() - self.start_time

class TestUserSession:
    def setUp(self):
        self.start_time = time.time()
        self.user_id = "user123"
        self.user_session = UserSession(self.user_id)

    def test_user_session_initialization(self):
        """Test initialization with a valid user_id."""
        assert self.user_session.user_id == self.user_id
        assert isinstance(self.user_session.start_time, float)

    def test_get_duration_initial(self):
        """Test duration immediately after creation."""
        time.sleep(1)  # Sleep for a short duration to ensure time difference
        duration = self.user_session.get_duration()
        print(duration)
        assert 0 <= duration < 1.1  # Duration should be between 0 and 1 seconds

    def test_get_duration_after_some_time(self):
        """Test duration after waiting for some time."""
        time.sleep(2)  # Sleep for 2 seconds
        duration = self.user_session.get_duration()
        assert 2 <= duration < 3.1  # Duration should be between 2 and 3 seconds

    def test_multiple_sessions_duration(self):
        """Test duration calculation for multiple sessions."""
        session1 = UserSession("user456")
        time.sleep(1)
        session2 = UserSession("user789")
        time.sleep(1)
        duration1 = session1.get_duration()
        duration2 = session2.get_duration()
        assert duration1 >= 1
        assert duration2 >= 1

    def test_session_duration_independence(self):
        """Test that duration is independent between sessions."""
        session1 = UserSession("user456")
        time.sleep(1)
        session2 = UserSession("user789")
        duration1 = session1.get_duration()
        duration2 = session2.get_duration()
        assert duration1 >= 1
        assert duration2 >= 0
        assert duration1 > duration2  # session1 started earlier

    def test_get_duration_is_positive(self):
        """Test that the duration is always positive."""
        duration = self.user_session.get_duration()
        assert duration >= 0

    def test_duration_calculation_after_long_time(self):
        """Test duration calculation after a long period."""
        time.sleep(5)  # Sleep for 5 seconds
        duration = self.user_session.get_duration()
        assert duration >= 5

    def test_get_duration_accuracy(self):
        """Test the accuracy of duration calculation."""
        time.sleep(1.5)  # Sleep for 1.5 seconds
        duration = self.user_session.get_duration()
        assert 1.5 <= duration < 2

    def test_duration_for_short_sleep(self):
        """Test duration for very short sleep periods."""
        time.sleep(0.1)  # Sleep for 0.1 seconds
        duration = self.user_session.get_duration()
        assert 0.1 <= duration < 0.2

    def test_duration_return_type(self):
        """Test that the duration is returned as a float."""
        duration = self.user_session.get_duration()
        assert isinstance(duration, float)
        
    def test_get_duration_with_no_sleep(self):
        """Test duration with no additional sleep."""
        duration = self.user_session.get_duration()
        print(f"Duration: {duration}")
        assert 0 <= duration < 1.5



if __name__ == "__main__":
    test_user_session = TestUserSession()
    test_user_session.setUp()
    
    # Run each test
    test_user_session.test_user_session_initialization()
    test_user_session.test_get_duration_initial()
    test_user_session.test_get_duration_after_some_time()
    test_user_session.test_multiple_sessions_duration()
    test_user_session.test_session_duration_independence()
    test_user_session.test_get_duration_is_positive()
    test_user_session.test_duration_calculation_after_long_time()
    test_user_session.test_duration_return_type()

    test_user_session.test_get_duration_accuracy()
    test_user_session.test_duration_for_short_sleep()
    test_user_session.test_get_duration_with_no_sleep()
