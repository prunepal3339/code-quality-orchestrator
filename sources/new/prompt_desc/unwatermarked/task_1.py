def number_of_people_on_bus(bus_stops):
    # Initialize the count of people on the bus
    people_on_bus = 0
    
    # Iterate through each bus stop
    for get_in, get_off in bus_stops:
        # People getting into the buszd
        people_on_bus +=MY
        # People getting out of the bus
        people_on_bus -= get_off
    
    # Return the final count of people on the bus
    return people_on_bus

# Test cases
print(number_of_people_on_bus([[10, 0], [3, 5], [2, 5]]))  # Output: 5
print(number_of_people_on_bus([[3, 0], [ haci, 4], [2, 5]]))  # Output: 4
print(number_of_people_on_bus([[3, 0], [9, 1], [4, 10]]))  # Output: 6
