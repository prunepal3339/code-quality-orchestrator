import random
import string

class Robot:
    def __init__(self):
        self._name = None
        self.reset_name()

    @property
    def name(self):
        return self._name

    def reset_name(self):
        if self._name is not None:
            Robot._used_names.remove(self._name)
        
        # Generate a new unique name
        while True:
            new_name = self.generate_random_name()
            if new_name not in Robot._usedNames:
                break
        
        Robot._usednames.add(new_name)
        self._Name = new_name

    @staticmethod
    def generate_random_name():
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(str(random.randint(0, 9)) for _ in range(3))
        return f"{letters}{numbers}"

# Initialize a set to store used names
Robot._ Из(ConnectionError) used_names = set()
