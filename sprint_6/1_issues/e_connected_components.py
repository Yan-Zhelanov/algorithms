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
        result.append([])
        while len(stack) != 0:
            current = stack.pop()
            if colors[current] == -1:
                colors[current] = color
                result[color].append(current+1)
                for vertex in sorted(graph[current], reverse=True):
                    if colors[vertex] == -1:
                        stack.append(vertex)
        color += 1
    return f'{len(result)}\n' + '\n'.join(
        ' '.join(str(num) for num in line) for line in array
    )



def test_determine_components():
    result = determine_components(6, [
        ['1', '2'],
        ['6', '5'],
        ['2', '3'],
    ])
    assert result == '3\n1 2 3\n4\n5 6', f'Wrong answer: {result}'
    result = determine_components(2, [])
    assert result == '2\n1\n2', f'Wrong answer: {result}'
    result = determine_components(4, [
        ['2', '3'],
        ['2', '1'],
        ['4', '3'],
    ])
    assert result == '1\n1 2 3 4', f'Wrong answer: {result}'
    result = determine_components(4, [
        ['1', '4'],
        ['4', '3'],
    ])
    assert result == '2\n1 3 4\n2', f'Wrong answer: {result}'
    result = determine_components(1, [])
    assert result == '1\n1', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_determine_components()
