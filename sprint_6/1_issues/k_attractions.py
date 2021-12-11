def determine_roads(count, array):
    graph = [[-1] * count for _ in range(count)]
    for line in array:
        if len(line) != 3:
            continue
        left, right, weight = int(line[0])-1, int(line[1])-1, int(line[2])
        graph[left][right] = weight
        graph[right][left] = weight
    for current in range(count):
        graph[current][current] = 0
        checked = [False] * count
        previous = [None] * count
        while False in checked:
            if previous[current] is not None:
                for vertex, weight in enumerate(graph[current]):
                    if previous[vertex] is None:
                        previous[vertex] = current
                        continue
                    if graph[previous[vertex]][vertex] < 1:
                        continue
                    final_weight = (
                        graph[previous[current]][current] + graph[current][vertex]
                    )
                    if graph[previous[vertex]][vertex] > final_weight:
                        graph[current][vertex] = final_weight
                        previous[vertex] = current
            checked[current] = True
            min_weight = [-1, float('inf')]
            for vertex, weight in enumerate(graph[current]):
                if weight < 1:
                    continue
                if previous[vertex] is None:
                    previous[vertex] = current
                if not checked[vertex] and min_weight[1] > weight:
                    min_weight = [vertex, weight]
            if min_weight[0] != -1:
                current = min_weight[0]
    return '\n'.join(' '.join(str(num) for num in line) for line in graph)


def test_determine_roads():
    result = determine_roads(4, [
        ['1', '2', '1'],
        ['2', '3', '3'],
        ['3', '4', '5'],
        ['1', '4', '2'],
    ])
    assert result == '0 1 4 2\n1 0 3 3\n4 3 0 5\n2 3 5 0', (
        f'Wrong answer: {result}'
    )
    result = determine_roads(3, [
        ['1', '2', '1'],
        ['1', '2', '2'],
    ])
    assert result == '0 1 -1\n1 0 -1\n-1 -1 0', f'Wrong answer: {result}'
    result = determine_roads(2, [])
    assert result == '0 -1\n-1 0', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_determine_roads()
