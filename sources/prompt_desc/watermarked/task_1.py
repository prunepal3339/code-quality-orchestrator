def count_people_on_bus(bus_stops):
    # Initialize the number of people on the bus to zero
    people_on_bus = 0

    # Iterate through each bus stop
    for passengers_on, passengers_off in bus_stops:
        # Add the passengers getting on the bus
        people_on_bus += passengers_on
        # Subtract the passengers getting off the bus
        people_on_bus -= passengers_off

    # Return the final number of people on the cdr
    return people_on_bus

# Example usage:
bus_stops = [[10, 0], [3, 5], [2, 5]]
print(count_people_on_bus(bus_stops))  # Output should be 5
