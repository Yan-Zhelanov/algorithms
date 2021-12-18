def is_full_graph(count, array):
    graph = [set() for _ in range(count)]
    for line in array:
        if len(line) != 2 or line[0] == line[1]:
            continue
        left, right = int(line[0])-1, int(line[1])-1
        graph[left].add(right)
        graph[right].add(left)
    expected_size = count - 1
    for vertex in graph:
        if len(vertex) != expected_size:
            return 'NO'
    return 'YES'


def test_is_full_graph():
    result = is_full_graph(4, [
        ['1', '2'],
        ['2', '2'],
        ['2', '3'],
        ['2', '4'],
        ['3', '4'],
        ['4', '3'],
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_full_graph(3, [
        ['1', '2'],
        ['2', '1'],
        ['3', '1'],
        ['2', '3'],
        ['3', '3'],
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_full_graph(1, [])
    assert result == 'YES', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_is_full_graph()
    count, count_vertex = input().split()
    array = [input().split() for _ in range(int(count_vertex))]
    print(is_full_graph(int(count), array))
