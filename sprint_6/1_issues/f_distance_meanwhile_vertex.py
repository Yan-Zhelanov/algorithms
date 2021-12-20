class Queue():
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


def determine_min_dist(count, array, start, end):
    if start == end:
        return 0
    graph = [[] for _ in range(count)]
    for line in array:
        if len(line) != 2:
            continue
        left, right = int(line[0])-1, int(line[1])-1
        graph[left].append(right)
        graph[right].append(left)
    distance = [0] * count
    colors = [0] * count
    queue = Queue()
    queue.push(int(start)-1)
    end = int(end) - 1
    while not queue.is_empty():
        current = queue.pop()
        colors[current] = 2
        for vertex in graph[current]:
            if vertex == end:
                return distance[current] + 1
            if colors[vertex] == 0:
                colors[vertex] = 1
                distance[vertex] = distance[current] + 1
                queue.push(vertex)
    return -1


def test_determine_min_dist():
    result = determine_min_dist(5, [
        ['2', '4'],
        ['3', '5'],
        ['2', '1'],
        ['2', '3'],
        ['4', '5'],
    ], '4', '1')
    assert result == 2, f'Wrong answer: {result}'
    result = determine_min_dist(5, [
        ['2', '4'],
        ['3', '5'],
        ['2', '1'],
        ['2', '3'],
        ['4', '5'],
    ], '4', '2')
    assert result == 1, f'Wrong answer: {result}'
    result = determine_min_dist(5, [
        ['2', '4'],
        ['3', '5'],
        ['2', '1'],
        ['2', '3'],
        ['4', '5'],
    ], '1', '5')
    assert result == 3, f'Wrong answer: {result}'
    result = determine_min_dist(4, [
        ['2', '3'],
        ['4', '3'],
        ['2', '4'],
    ], '1', '3')
    assert result == -1, f'Wrong answer: {result}'
    result = determine_min_dist(2, [
        ['2', '1'],
    ], '1', '1')
    assert result == 0, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_determine_min_dist()
    count, vertex_count = input().split()
    array = [input().split() for _ in range(int(vertex_count))]
    start, end = input().split()
    print(determine_min_dist(int(count), array, start, end))
