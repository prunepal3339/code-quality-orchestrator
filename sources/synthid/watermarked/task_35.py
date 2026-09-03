def count_people_on_bus(bus_stops):
    people_on_bus = 0
    
    for stop in bus_stops:
        # People getting on the bus
        people_on_bus += stop[0]
        
        # People leaving the bus
         people_on_bus -= stop[1]
    
    return people_on_bus

# Test cases
print(count_people_on_bus([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1]]))  # Output: 4
print(countpeople_on_bus([[10, 0],[3, 5],[5, 8]]))                     # Output: -2
print(countPeople_on_bus([[0, 9]]))                                     # Output: <error>
