def determine_components(count, array):
    graph = [[] for _ in range(count)]
    for line in array:
        if len(line) == 2:
            left, right = int(line[0])-1, int(line[1])-1
            graph[left].append(right)
            graph[right].append(left)
    colors = [-1] * count
    color = 0
    result = []
    for current in range(count):
        stack = [current]
        changed = False
        component = []
        while len(stack) != 0:
            current = stack.pop()
            if colors[current] != -1:
                continue
            changed = True
            component.append(current+1)
            colors[current] = color
            for vertex in graph[current]:
                if colors[vertex] != -1:
                    continue
                stack.append(vertex)
        if changed:
            color += 1
            result.append('\n')
            for num in sorted(component):
                result.append(num)
    return f'{color}' + ''.join(
        num if num == '\n'
        else f'{str(num)} '
        for num in result
    )


def test_determine_components():
    result = determine_components(6, [
        ['1', '2'],
        ['6', '5'],
        ['2', '3'],
    ])
    assert result == '3\n1 2 3 \n4 \n5 6 ', f'Wrong answer: {result}'
    result = determine_components(2, [])
    assert result == '2\n1 \n2 ', f'Wrong answer: {result}'
    result = determine_components(4, [
        ['2', '3'],
        ['2', '1'],
        ['4', '3'],
    ])
    assert result == '1\n1 2 3 4 ', f'Wrong answer: {result}'
    result = determine_components(4, [
        ['1', '4'],
        ['4', '3'],
    ])
    assert result == '2\n1 3 4 \n2 ', f'Wrong answer: {result}'
    result = determine_components(1, [])
    assert result == '1\n1 ', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_components()
    count, count_vertex = input().split()
    array = [input().split() for _ in range(int(count_vertex))]
    print(determine_components(int(count), array))
