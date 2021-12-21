def is_optimal_map(array):
    graph = [[] for _ in range(len(array)+1)]
    for index_line in range(len(array)):
        for index_char in range(len(array[index_line])):
            if array[index_line][index_char] == 'R':
                graph[index_line].append(index_line+index_char+1)
                continue
            graph[index_line+index_char+1].append(index_line)
    colors = [0] * len(graph)
    stack = []
    for current in range(len(graph)-1, -1, -1):
        if colors[current] != 0:
            continue
        stack.append(current)
        while len(stack) != 0:
            current = stack.pop()
            if colors[current] == 1:
                colors[current] = 2
                continue
            colors[current] = 1
            stack.append(current)
            for vertex in graph[current]:
                if colors[vertex] == 1:
                    return 'NO'
                if colors[vertex] == 2:
                    continue
                stack.append(vertex)
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
    result = is_optimal_map([
        'RRBRRBRRR',
        'BBBBBBRB',
        'BBRBRRR',
        'RRBRRR',
        'RBRRR',
        'BBRR',
        'RRR',
        'RR',
        'B',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    print('All tests passed!')


def test_speed_is_optimal_map():
    with open('output.txt', 'r') as array:
        array = [line[:-2] for line in array]
        is_optimal_map(array)


def create_output_for_test():
    from random import choice
    count = 3000
    text = (
        '\n'.join([
            ''.join(choice('RB') for _ in range(count-index-1))
            for index in range(count-1)
        ])
    )
    with open('output.txt', 'w') as output:
        output.writelines(text)


if __name__ == '__main__':
    # test_is_optimal_map()
    # create_output_for_test()
    test_speed_is_optimal_map()
    # count = int(input())
    # array = [input() for _ in range(count-1)]
    # print(is_optimal_map(array))
