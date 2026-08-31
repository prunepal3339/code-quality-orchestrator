def isValidWalk(walk):
    # Check if the walk length is exactly 10 minutes
    if len(walk) != 10:
        return False
    
    # Initialize coordinates at the starting point
    x, y = 0, 0
    
    # Dictionary to map directions to coordinate changes
    direction_map = {
        'n': (0, 1),
        's': (0, -1),
        'e': (1, 0),
        'w': (-1, 0)
    }
    
    # Traverse the walk and update coordinates
    for direction in walk:
        dx, dy = direction_map[direction]
        x += dx
        y += dy
    
    # Check if the final position is the starting point
    return x == 0 and y == 0
