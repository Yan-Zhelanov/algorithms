from math import sqrt


def determine_best_exit_metro(metro_stations, bus_stations):
    size = len(metro_stations) + 1
    bests = [0] * size
    index = 1
    while index < size:
        location_x = int(metro_stations[index-1][0])
        location_y = int(metro_stations[index-1][1])
        for station in bus_stations:
            distance = sqrt(
                (location_x - int(station[0]))**2
                + (location_y - int(station[1]))**2
            )
            if distance <= 20:
                bests[index] = bests[index] + 1
        index = index + 1
    return bests.index(max(bests))


def test_determine_best_exit_metro():
    result = determine_best_exit_metro(
        [[-1, 0], [1, 0], [2, 5]],
        [[10, 0], [20, 0], [22, 5]],
    )
    assert result == 3, f'Wrong answer: {result}'
    result = determine_best_exit_metro(
        [[0, 5], [10, 0], [1, 2]],
        [[10, 0], [20, 0], [22, 5]],
    )
    assert result == 2, f'Wrong answer: {result}'
    result = determine_best_exit_metro(
        [[10, 0], [2, 0], [2, 5]],
        [[10, 0], [20, 0], [22, 5]],
    )
    assert result == 1, f'Wrong answer: {result}'
    result = determine_best_exit_metro(
        [[10, 0]],
        [[10, 0], [20, 0], [22, 5]],
    )
    assert result == 1, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_best_exit_metro()
    count = int(input())
    metro_stations = [input().split() for _ in range(count)]
    count = int(input())
    bus_stations = [input().split() for _ in range(count)]
    print(determine_best_exit_metro(metro_stations, bus_stations))
