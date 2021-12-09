def topological_sort(count, array):
    result = []
    graph = [[] for _ in range(count)]
    for line in array:
        if len(line) == 2:
            left, right = int(line[0])-1, int(line[1])-1
            graph[left].append(right)
    colors = [0] * count
    stack = []
    for current in range(count):
        stack.append(current)
        while len(stack) != 0:
            current = stack.pop()
            if colors[current] == 0:
                colors[current] = 1
                stack.append(current)
                for vertex in sorted(graph[current], reverse=True):
                    if colors[vertex] == 0:
                        stack.append(vertex)
            elif colors[current] == 1:
                colors[current] = 2
                result.append(current+1)
    return ' '.join(str(num) for num in result)


def test_topological_sort():
    result = topological_sort(4, [])
    assert result == '1 2 3 4', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_topological_sort()
    count, count_vertex = input().split()
    array = [input().split() for _ in range(int(count_vertex))]
    print(topological_sort(int(count), array))
