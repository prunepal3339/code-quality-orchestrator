def count_people_on_bus(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
