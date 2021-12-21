def is_bipartite(count, array):
    graph = [[] for _ in range(count)]
    for line in array:
        if len(line) == 2:
            left, right = int(line[0])-1, int(line[1])-1
            graph[left].append(right)
            graph[right].append(left)
    left = set()
    right = set()
    for current in range(count):
        if current not in left and current not in right:
            left.add(current)
            for vertex in graph[current]:
                if vertex in left:
                    return 'NO'
                right.add(vertex)
        if current in left:
            for vertex in graph[current]:
                if vertex in left:
                    return 'NO'
                right.add(vertex)
        if current in right:
            for vertex in graph[current]:
                if vertex in right:
                    return 'NO'
                left.add(vertex)
    return 'YES'


def test_is_bipartite():
    result = is_bipartite(3, [
        ['1', '2'],
        ['2', '3'],
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_bipartite(3, [
        ['1', '2'],
        ['2', '3'],
        ['1', '3'],
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_bipartite(3, [
        ['1', '2'],
        ['1', '3'],
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_bipartite(4, [
        ['1', '2'],
        ['2', '3'],
        ['3', '4'],
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_bipartite(4, [
        ['1', '2'],
        ['2', '3'],
        ['3', '4'],
        ['4', '2'],
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_bipartite(1, [])
    assert result == 'YES', f'Wrong answer: {result}'
    print('All tests passed')


if __name__ == '__main__':
    test_is_bipartite()
    count, vertex_count = input().split()
    array = [input().split() for _ in range(int(vertex_count))]
    print(is_bipartite(int(count), array))
