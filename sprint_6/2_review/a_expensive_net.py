def determine_max_weight(count, array):
    if count == 1:
        return 0
    if len(array) == 0:
        return 'Oops! I did it again'
    graph = [{} for _ in range(count)]
    for line in array:
        if len(line) != 3:
            continue
        left, right, weight = int(line[0])-1, int(line[1])-1, int(line[2])
        if graph[left].get(right, 0) >= weight:
            continue
        graph[left][right] = weight
        graph[right][left] = weight
    not_visited = set(num for num in range(count))
    visited = set()
    edges = []
    max_weight = 0
    current = list(graph[0].keys())[0]
    while len(not_visited) != 0:
        not_visited.remove(current)
        visited.add(current)
        for vertex in graph[current]:
            if vertex in visited:
                continue
            edges.append([current, vertex, graph[current][vertex]])
        edges.sort(key=lambda item: item[2])
        if len(edges) == 0 or len(not_visited) == 0:
            break
        current = edges.pop()
        while current[1] in visited and len(edges) != 0:
            current = edges.pop()
        if current[1] in visited and len(edges) != 0:
            break
        max_weight += current[2]
        current = current[1]
    if len(not_visited) != 0:
        return 'Oops! I did it again'
    return max_weight


def test_determine_max_weight():
    result = determine_max_weight(10, [
        ['9', '10', '4'],
        ['2', '2', '4'],
        ['4', '2', '8'],
        ['10', '5', '3'],
        ['1', '10', '6'],
        ['7', '4', '2'],
        ['10', '10', '6'],
        ['3', '7', '4'],
        ['8', '9', '4'],
        ['8', '10', '7'],
        ['6', '10', '10'],
        ['2', '8', '8'],
        ['3', '8', '1'],
        ['3', '10', '3'],
        ['9', '5', '8'],
        ['10', '10', '2'],
        ['1', '8', '1'],
        ['10', '1', '5'],
        ['3', '6', '10'],
        ['9', '10', '8'],
    ])
    assert result == 69, f'Wrong answer: {result}'
    result = determine_max_weight(5, [
        ['1', '2', '3'],
        ['2', '2', '2'],
        ['2', '3', '2'],
        ['3', '4', '4'],
        ['4', '5', '3'],
        ['5', '2', '1'],
    ])
    assert result == 12, f'Wrong answer: {result}'
    result = determine_max_weight(4, [
        ['1', '2', '5'],
        ['1', '3', '6'],
        ['2', '4', '8'],
        ['3', '4', '3'],
    ])
    assert result == 19, f'Wrong answer: {result}'
    result = determine_max_weight(3, [
        ['1', '2', '1'],
        ['1', '2', '2'],
        ['2', '3', '1'],
    ])
    assert result == 3, f'Wrong answer: {result}'
    result = determine_max_weight(5, [
        ['1', '2', '4'],
        ['2', '1', '2'],
    ])
    assert result == 'Oops! I did it again', f'Wrong answer: {result}'
    result = determine_max_weight(2, [])
    assert result == 'Oops! I did it again', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_determine_max_weight()
    count, count_vertex = input().split()
    array = [input().split() for _ in range(int(count_vertex))]
    print(determine_max_weight(int(count), array))
