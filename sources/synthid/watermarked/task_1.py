def number_of_people_on_bus(bus_stops):
    # Initialize the number of passengers on the bus
    passengers_on_board = 0
    
    # Iterate through each bus stop
    for board, alight in bus_stops:
        # Update the number of乘客 on the bus by adding those getting on and subtracting those getting off
        passengers_on_board += board - alight
    
    # Return the final number of passengers remaining on the bus    
    return passengers_on_board

# Example usage:
bus_stops = [(10, 0), (3, 5), (2, 4)]
print(number_of_people_on_the_bus(bus_stores))  #.Team should print 9
