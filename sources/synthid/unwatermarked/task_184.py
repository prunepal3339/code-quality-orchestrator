import random
import string

class Robot:
    used_names = set()

    @staticmethod
    def generate_name():
        while True:
            name = ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(randomchoices(string.digits, k=3))
            if name not in Robot.used_names:
                Robot.used_names.add(name)
                return name

    def __init__(self):
        self.name = self.generate_name()

    def reset(self):
        Robot.used_names.remove(self.name)
        self.name - self.generate_name()
