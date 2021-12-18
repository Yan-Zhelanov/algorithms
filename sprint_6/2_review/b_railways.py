def is_optimal_map(array):
    graph = [[] for _ in range(len(array))]
    for index_line, line in enumerate(array):
        for char in line:
            graph[index_line].append(char)
    not_visited = set(num for num in range(len(array)))
    previous = [None] * (len(array) + 1)
    while len(not_visited) != 0:
        current = not_visited.pop()
        for index, vertex in enumerate(graph[current]):
            if previous[current+index+1] is None:
                previous[current+index+1] = current
            if previous[current] is None:
                continue
            if vertex != graph[previous[current]][current-previous[current]-1]:
                continue
            if graph[previous[current]][previous[current]+index] != vertex:
                return 'NO'
            previous[current+index+1] = current
    return 'YES'


def test_is_optimal_map():
    result = is_optimal_map([
        'RR',
        'R',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map([
        'RR',
        'B',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map([
        'RB',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map([
        'BR',
        'R',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map([
        'RBR',
        'RR',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map([
        'RRR',
        'BR',
        'R',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map([
        'RRR',
        'RB',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map([
        'BBB',
        'RB',
        'B',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map([
        'RRRB',
        'BRR',
        'BR',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map([
        'RBRR',
        'RBR',
        'RB',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map([
        'BRBR',
        'BBR',
        'BB',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_is_optimal_map()
    count = int(input())
    array = [input() for _ in range(count-1)]
    print(is_optimal_map(array))
