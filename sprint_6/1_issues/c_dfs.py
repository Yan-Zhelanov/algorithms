def bypass_graph(count, array, start):
    array.sort()
    result = []
    stack = [start]
    colors = ['w'] * count
    while len(stack) != 0:
        current = stack.pop()
        if colors[int(current)-1] == 'w':
            colors[int(current)-1] = 'g'
            stack.append(current)
            result.append(current)
            for edge in array:
                if current in edge:
                    index = edge.index(current)
                    if colors[edge[index-1]] == 'w':
                        stack.append(str(count-index))
        elif colors[int(current)-1] == 'g':
            colors[int(current)-1] = 'b'
    return ' '.join(result)


def test_bypass_graph():
    result = bypass_graph(4, [
        ['3', '2'],
        ['4', '3'],
        ['1', '4'],
        ['1', '2'],
    ], '1')
    assert result == '1 2 3 4', f'Wrong answer: {result}'
    result = bypass_graph(4, [
        ['3', '2'],
        ['4', '3'],
        ['1', '4'],
        ['1', '2'],
    ], '3')
    assert result == '3 2 1 4', f'Wrong answer: {result}'
    result = bypass_graph(2, [
        ['1', '2'],
    ], '1')
    assert result == '1 2', f'Wrong answer: {result}'
    result = bypass_graph(1, [
        ['1', '1'],
    ], '1')
    assert result == '1', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_bypass_graph()
    count, edges = input().split()
    array = [input().split() for _ in range(int(edges))]
    print(bypass_graph(int(count), array, input()))
