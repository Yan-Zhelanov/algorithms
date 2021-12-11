def determine_min_roads(count, array, start):
    graph = [[-1] * count for _ in range(count)]
    for line in array:
        left, right, weight = int(line[0])-1, int(line[1])-1, int(line[2])
        graph[left][right] = weight
        graph[right][left] = weight
    checked = [False] * count
    previous = [None] * count
    current = int(start) - 1
    while False in checked:
        if previous[current] is not None:
            pass
        for vertex, weight in graph[current]:
            if previous[vertex] is None:
                previous[vertex] = current


def test_determine_min_roads():
    result = determine_min_roads(6, [
        ['1', '2', '5'],
        ['1', '3', '15'],
        ['1', '4', '10'],
        ['3', '4', '3'],
        ['3', '5', '6'],
        ['2', '4', '2'],
        ['2', '6', '11'],
        ['4', '1', '3'],
        ['4', '3', '4'],
        ['4', '5', '3'],
        ['4', '6', '4'],
        ['5', '3', '2'],
        ['5', '6', '6'],
    ], '1')
    assert result == '0 5 11 7 10 11', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_determine_min_roads()
