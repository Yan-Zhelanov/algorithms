def is_optimal_map(array):
    visited = [False] * (len(array)+1)
    stack = []
    for current in range(len(array), -1, -1):
        if visited[current]:
            continue
        stack.append(current)
        while len(stack) != 0:
            current = stack.pop()
            if visited[current]:
                visited[current] = False
                continue
            stack.append(current)
            visited[current] = True
            for vertex in range(current-1, -1, -1):
                index_current = current - vertex - 1
                if array[vertex][index_current] != 'B':
                    continue
                if visited[vertex]:
                    return 'NO'
                stack.append(vertex)
            if current == len(array):
                continue
            for index_vertex in range(len(array[current])):
                vertex = current + index_vertex + 1
                if array[current][index_vertex] != 'R':
                    continue
                if visited[vertex]:
                    return 'NO'
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
    # test_speed_is_optimal_map()
    count = int(input())
    array = [input() for _ in range(count-1)]
    print(is_optimal_map(array))
