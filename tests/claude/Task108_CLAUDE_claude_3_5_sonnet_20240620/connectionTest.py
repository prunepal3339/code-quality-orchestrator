import unittest
import Pyro4

class TestRemoteObject(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the proxy to the remote object
        cls.uri = "PYRO:remote_object@192.168.1.148:9090"
        cls.remote_object = Pyro4.Proxy(cls.uri)

    def test_get_initial_value(self):
        # Test the initial value of the remote object
        value = self.remote_object.get_value()
        self.assertEqual(value, 0, "Initial value should be 0")

    def test_set_value(self):
        # Test setting a new value
        new_value = 10
        self.remote_object.set_value(new_value)
        value = self.remote_object.get_value()
        self.assertEqual(value, new_value, f"Value should be {new_value}")

    def test_increment(self):
        # Test incrementing the value
        self.remote_object.set_value(5)  # Set a known value
        self.remote_object.increment()
        value = self.remote_object.get_value()
        self.assertEqual(value, 6, "Value should be incremented by 1")

    def test_multiple_increments(self):
        # Test incrementing multiple times
        self.remote_object.set_value(0)  # Reset to 0
        for _ in range(5):
            self.remote_object.increment()
        value = self.remote_object.get_value()
        self.assertEqual(value, 5, "Value should be incremented 5 times")

if __name__ == "__main__":
    unittest.main()