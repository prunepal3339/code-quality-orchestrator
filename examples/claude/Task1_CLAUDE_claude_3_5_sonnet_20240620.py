
def bus_stops(bus_stops):
    return sum(on - off for on, off in bus_stops)
