def bus_stops(stops):
    return sum(on - off for on, off in stops)


def test_bus_stops():
    # Test Case 1: Basic scenario with a few stops
    stops = [(3, 0), (2, 1), (5, 2), (1, 4)]
    assert bus_stops(stops) == 4

    # Test Case 2: Scenario where more people get off than get on at some stops
    stops = [(10, 0), (3, 5), (2, 1), (7, 10)]
    assert bus_stops(stops) == 6

    # Test Case 3: Edge case where no one gets on or off the bus
    stops = [(0, 0), (0, 0), (0, 0), (0, 0)]
    assert bus_stops(stops) == 0

    # Test Case 4: Mixed scenario with different numbers of people getting on and off
    stops = [(5, 0), (3, 2), (8, 4), (2, 1)]
    assert bus_stops(stops) == 11

    # Test Case 5: Scenario with some stops involving no people getting on or off
    stops = [(7, 0), (0, 0), (5, 3), (3, 7), (4, 0)]
    assert bus_stops(stops) == 9

    # Test Case 6: Scenarios where the number of people getting on and off balances out to zero at some stops
    stops = [(1, 0), (0, 0), (1, 1), (0, 0), (1, 0), (0, 1)]
    assert bus_stops(stops) == 1

    # Test Case 7: Large numbers to ensure the sum is calculated correctly
    stops = [(100, 0), (50, 30), (25, 25), (10, 15), (0, 10)]
    assert bus_stops(stops) == 105

    # Test Case 8: Ensure correct processing where different numbers of people get on and off
    stops = [(3, 0), (0, 2), (2, 1), (0, 1), (1, 0)]
    assert bus_stops(stops) == 2

    # Test Case 9: Verifies that the bus ends up empty after the final stop
    stops = [(50, 0), (0, 50)]
    assert bus_stops(stops) == 0

    # Test Case 10: Varied inputs, ensuring correct calculation
    stops = [(6, 0), (2, 3), (1, 5), (7, 2)]
    assert bus_stops(stops) == 6

test_bus_stops()
