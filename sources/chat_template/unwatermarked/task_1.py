def number_of_people(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
