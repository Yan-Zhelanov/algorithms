def is_optimal_map(count, array):
    visited = set()
    stack = []
    for current in range(count-1, -1, -1):
        if current in visited:
            continue
        stack.append(current)
        while len(stack) != 0:
            current = stack.pop()
            if current in visited:
                visited.remove(current)
                continue
            stack.append(current)
            visited.add(current)
            for vertex in range(current-1, -1, -1):
                index_current = current - vertex - 1
                if array[vertex][index_current] != 'B':
                    continue
                if vertex in visited:
                    return 'NO'
                stack.append(vertex)
            if current == count-1:
                continue
            for index_vertex in range(len(array[current])):
                vertex = current + index_vertex + 1
                if array[current][index_vertex] != 'R':
                    continue
                if vertex in visited:
                    return 'NO'
                stack.append(vertex)
    return 'YES'


def test_is_optimal_map():
    result = is_optimal_map(3, [
        'RR',
        'R',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map(3, [
        'RR',
        'B',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map(3, [
        'RB',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map(3, [
        'BR',
        'R',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map(4, [
        'RBR',
        'RR',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map(4, [
        'RRR',
        'BR',
        'R',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map(4, [
        'RRR',
        'RB',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map(4, [
        'BBB',
        'RB',
        'B',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map(5, [
        'RRRB',
        'BRR',
        'BR',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map(5, [
        'RBRR',
        'RBR',
        'RB',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map(5, [
        'BRBR',
        'BBR',
        'BB',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map(10, [
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
    print(is_optimal_map(count, array))
