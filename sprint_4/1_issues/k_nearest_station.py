from math import sqrt


def determine_best_exit_metro(metro_stations, bus_stations):
    bests = {}
    for index, metro in enumerate(metro_stations):
        for station in bus_stations:
            distance = sqrt(
                (metro[0] - station[0])**2 + (metro[1] - station[1])**2
            )
            if distance <= 20:
                bests[index+1] = bests.get(index+1, 0) + 1
    return list(bests.keys())[list(bests.values()).index(max(bests.values()))]


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
    metro_stations = [list(map(int, input().split())) for _ in range(count)]
    count = int(input())
    bus_stations = [list(map(int, input().split())) for _ in range(count)]
    print(determine_best_exit_metro(metro_stations, bus_stations))
