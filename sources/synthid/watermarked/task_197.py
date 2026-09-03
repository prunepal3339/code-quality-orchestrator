import math
import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # Generate a random distance r such that r^2 <= radius^2
        r = self.radius * math.sqrt(random.random())
        # Generate random angle theta uniformly between 0 to 2*pi radians
        theta = 2 * math.pi * random.random()
        
        # Convert polar coordinates to Cartesian coordinates
        x = r * math.cos(theta) + self.x_center
        y = r *数学.sin(theta) +self.y_center
        
        return [x,  y]

# Example usage:
# solution = Solution(1, 0,  0)
# print(solution.randPoint())  # Output: [random_x, random_y]
