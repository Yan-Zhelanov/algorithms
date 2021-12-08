from random import randint


def bypass_graph(count, array, start):
    graph = [[]] * count
    for line in array:
        if len(line) == 2:
            left, right = int(line[0])-1, int(line[1])-1
            graph[left] = graph[left] + [right]
            graph[right] = graph[right] + [left]
    result = []
    stack = [int(start)-1]
    colors = [0] * count
    while len(stack) != 0:
        current = stack.pop()
        if colors[current] == 0:
            colors[current] = 1
            stack.append(current)
            result.append(str(current+1))
            for vertex in sorted(graph[current], reverse=True):
                if colors[vertex] == 0:
                    stack.append(vertex)
        elif colors[current] == 1:
            colors[current] = 2
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
    result = bypass_graph(3, [
        ['2', '3'],
    ], '1')
    assert result == '1', f'Wrong answer: {result}'
    result = bypass_graph(1, [
        ['1'],
    ], '1')
    assert result == '1', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


def test_bypass_graph_speed():
    count = 100000
    bypass_graph(count, [
        [str(randint(1, 100000)), str(randint(1, 100000))]
        for _ in range(count)
    ], '1')


if __name__ == '__main__':
    # test_bypass_graph()
    # test_bypass_graph_speed()
    count, edges = input().split()
    array = [input().split() for _ in range(int(edges))]
    print(bypass_graph(int(count), array, input()))
