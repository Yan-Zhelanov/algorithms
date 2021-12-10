class Queue:
    def __init__(self):
        self.head = []
        self.tail = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        self.head.append(value)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Queue is empty!')
        if self.tail == []:
            for _ in range(len(self.head)):
                self.tail.append(self.head.pop())
        self.size -= 1
        return self.tail.pop()


def bypass_graph(count, array, start):
    if count == 1:
        return start
    graph = [[] for _ in range(count)]
    for line in array:
        if len(line) == 2:
            left, right = int(line[0])-1, int(line[1])-1
            graph[left].append(right)
            graph[right].append(left)
    roads = [None] * count
    colors = [0] * count
    result = []
    queue = Queue()
    queue.push(int(start)-1)
    while not queue.is_empty():
        current = queue.pop()
        if colors[current] == 0:
            colors[current] = 1
            if roads[current] is None:
                roads[current] = 0
            result.append(str(current+1))
            for vertex in sorted(graph[current]):
                if colors[vertex] == 0:
                    roads[vertex] = roads[current] + 1
                    queue.push(vertex)
        elif colors[current] == 1:
            colors[current] = 2
    return ' '.join(result)


def test_bypass_graph():
    result = bypass_graph(4, [
        ['1', '2'],
        ['2', '3'],
        ['3', '4'],
        ['1', '4'],
    ], '3')
    assert result == '3 2 4 1', f'Wrong answer: {result}'
    result = bypass_graph(6, [
        ['1', '2'],
        ['2', '1'],
        ['1', '4'],
        ['4', '3'],
        ['6', '5'],
    ], '1')
    assert result == '1 2 4 3', f'Wrong answer: {result}'
    result = bypass_graph(2, [], '1')
    assert result == '1', f'Wrong answer: {result}'
    result = bypass_graph(1, [], '2')
    assert result == '2', f'Wrong answer: {result}'
    result = bypass_graph(3, [], '3')
    assert result == '3', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_bypass_graph()
    count, count_vertex = input().split()
    array = [input().split() for _ in range(int(count_vertex))]
    print(bypass_graph(int(count), array, input()))
