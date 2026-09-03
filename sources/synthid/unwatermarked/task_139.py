import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of your circle: "))
        if radius < 0:
            print("Please enter a non-negative value for the radius.")
        else:
            area = calculate_circle_area(circle_radius)
            print(f"The area of the circle with radius {radius} is {area:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the diameter.")
