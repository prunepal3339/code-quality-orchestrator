def build_tower(floors):
    if floors <= 0:
        return []

    # Calculate the width of the base of the tower
    base_width = 2 * floors - 1
    
    # Initialize an empty list to store each floor of the tower
    tower = []
    
    for i in range(floors):
        # Calculate the spaces needed on each side of the current floor
        spaces = ' ' * (floors - i - 1)
        # Create the current floor string and add it to the tower list
        floor = spaces + '*' * (2 * i + 1) + spaces
        tower.append(floor)
    
    return tower

# Example usage:
print(build_tower(3))
print(build_tower(6))
