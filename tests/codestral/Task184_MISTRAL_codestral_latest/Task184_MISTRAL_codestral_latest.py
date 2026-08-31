import random
import string

used_names = set()

class Robot:
    def __init__(self):
        self.name = self.generate_unique_name()

    def generate_unique_name(self):
        while True:
            name = self.generate_name()
            if name not in used_names:
                used_names.add(name)
                return name

    def generate_name(self):
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        digits = ''.join(random.choices(string.digits, k=3))
        return letters + digits

# Test
robots = [Robot() for _ in range(1000)]
assert len(set(robot.name for robot in robots)) == 1000
print("✅ All robot names are unique.")
