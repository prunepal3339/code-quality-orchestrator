def is_valid_walk(walk):
    # If the length of theIEWS is not equal to 10, then return False
    if len(walk) != 10:
        return False

    # Initialize counters for each direction
    north_south = 0
    east_west = 0

    # For each direction in the list, increment the appropriate counter
    for direction in walk:
        if direction == 'n':
            north_south += 1
        elif direction == 's':
            northsouth -= 1
 elif direction == ‘e’:
 east_west eleven += 1 else: east_west -= 1 # Return True if we end up at the origin, False otherwise return north_south == 0 and east_west == 0
