def determine_time(count, array):
    graph = [[] for _ in range(count)]
    for line in array:
        if len(line) == 2:
            left, right = int(line[0])-1, int(line[1])-1
            graph[left].append(right)
    time = 0
    stack = [0]
    result = [[] for _ in range(count)]
    colors = [0] * count
    while len(stack) != 0:
        current = stack.pop()
        if colors[current] == 0:
            colors[current] = 1
            result[current].append(time)
            stack.append(current)
            time += 1
            for vertex in sorted(graph[current], reverse=True):
                if colors[vertex] == 0:
                    stack.append(vertex)
        elif colors[current] == 1:
            colors[current] = 2
            result[current].append(time)
            time += 1
    return '\n'.join(
        ' '.join(str(time) for time in times)
        for times in result if times != []
    )


def test_determine_time():
    result = determine_time(6, [
        ['2', '6'],
        ['1', '6'],
        ['3', '1'],
        ['2', '5'],
        ['4', '3'],
        ['3', '2'],
        ['1', '2'],
        ['1', '4'],
    ])
    assert result == '0 11\n1 6\n8 9\n7 10\n2 3\n4 5', (
        f'Wrong answer: {result}'
    )
    result = determine_time(1, [
        ['1'],
    ])
    assert result == '0 1', (
        f'Wrong answer: {result}'
    )
    result = determine_time(3, [
        ['2', '3'],
    ])
    assert result == '0 1', (
        f'Wrong answer: {result}'
    )
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_time()
    count, vertex_count = input().split()
    array = [input().split() for _ in range(int(vertex_count))]
    print(determine_time(int(count), array))
