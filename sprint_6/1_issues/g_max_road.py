class Queue:
    def __init__(self):
        self.tail = []
        self.head = []
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


def determine_max_road(count, array, start):
    graph = [[] for _ in range(count)]
    for line in array:
        if len(line) == 2:
            left, right = int(line[0])-1, int(line[1])-1
            graph[left].append(right)
            graph[right].append(left)
    colors = [0] * count
    roads = [None] * count
    max_road = 0
    queue = Queue()
    queue.push(int(start)-1)
    while not queue.is_empty():
        current = queue.pop()
        if colors[current] == 0:
            colors[current] = 1
            queue.push(current)
            if roads[current] is None:
                roads[current] = 0
            for vertex in graph[current]:
                if colors[vertex] == 0:
                    if roads[vertex] is None:
                        roads[vertex] = roads[current] + 1
                        if roads[vertex] > max_road:
                            max_road = roads[vertex]
                    queue.push(vertex)
    return max_road


def test_determine_max_road():
    result = determine_max_road(5, [
        ['2', '1'],
        ['4', '5'],
        ['4', '3'],
        ['3', '2'],
    ], '2')
    assert result == 3, f'Wrong answer: {result}'
    result = determine_max_road(3, [
        ['3', '1'],
        ['1', '2'],
        ['2', '3'],
    ], '1')
    assert result == 1, f'Wrong answer: {result}'
    result = determine_max_road(6, [
        ['6', '1'],
        ['1', '3'],
        ['5', '1'],
        ['3', '5'],
        ['3', '4'],
        ['6', '5'],
        ['5', '2'],
        ['6', '2'],
    ], '4')
    assert result == 3, f'Wrong answer: {result}'
    result = determine_max_road(1, [], '1')
    assert result == 0, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_max_road()
    count, vertex_count = input().split()
    array = [input().split() for _ in range(int(vertex_count))]
    print(determine_max_road(int(count), array, input()))
