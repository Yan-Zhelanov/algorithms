class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def key(self, item):
        return item[2]

    def heapify_down(self, index):
        heap = self.heap
        left, right = index * 2, index * 2 + 1
        if right < self.size:
            max_index = heap.index(
                max(heap[index], heap[left], heap[right], key=self.key)
            )
        elif left < self.size:
            max_index = heap.index(
                max(heap[index], heap[left], key=self.key)
            )
        else:
            return
        if max_index == index:
            return
        heap[index], heap[max_index] = heap[max_index], heap[index]
        self.heapify_down(max_index)

    def heapify_up(self, index):
        heap = self.heap
        parent = index // 2
        if self.key(heap[parent]) >= self.key(heap[index]):
            return
        heap[parent], heap[index] = heap[index], heap[parent]
        self.heapify_up(parent)

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('MaxHeap is empty!')
        heap = self.heap
        heap[0], heap[-1] = heap[-1], heap[0]
        removable = heap.pop()
        self.size -= 1
        self.heapify_down(0)
        return removable


def determine_max_weight(count, array):
    if count == 1:
        return 0
    if len(array) == 0:
        return 'Oops! I did it again'
    graph = [{} for _ in range(count)]
    for line in array:
        if len(line) != 3:
            continue
        left, right, weight = int(line[0])-1, int(line[1])-1, int(line[2])
        if graph[left].get(right, 0) >= weight:
            continue
        graph[left][right] = weight
        graph[right][left] = weight
    visited = set()
    edges = MaxHeap()
    max_weight = 0
    current = list(graph[0].keys())[0]
    while len(visited) != count:
        visited.add(current)
        for vertex in graph[current]:
            if vertex in visited:
                continue
            edges.push([current, vertex, graph[current][vertex]])
        if edges.is_empty() or len(visited) == count:
            break
        while True:
            current = edges.pop()
            if current[1] in visited:
                if edges.is_empty():
                    return 'Oops! I did it again'
                continue
            break
        max_weight += current[2]
        current = current[1]
    if len(visited) != count:
        return 'Oops! I did it again'
    return max_weight


def test_determine_max_weight():
    result = determine_max_weight(10, [
        ['9', '10', '4'],
        ['2', '2', '4'],
        ['4', '2', '8'],
        ['10', '5', '3'],
        ['1', '10', '6'],
        ['7', '4', '2'],
        ['10', '10', '6'],
        ['3', '7', '4'],
        ['8', '9', '4'],
        ['8', '10', '7'],
        ['6', '10', '10'],
        ['2', '8', '8'],
        ['3', '8', '1'],
        ['3', '10', '3'],
        ['9', '5', '8'],
        ['10', '10', '2'],
        ['1', '8', '1'],
        ['10', '1', '5'],
        ['3', '6', '10'],
        ['9', '10', '8'],
    ])
    assert result == 69, f'Wrong answer: {result}'
    result = determine_max_weight(5, [
        ['1', '2', '3'],
        ['2', '2', '2'],
        ['2', '3', '2'],
        ['3', '4', '4'],
        ['4', '5', '3'],
        ['5', '2', '1'],
    ])
    assert result == 12, f'Wrong answer: {result}'
    result = determine_max_weight(4, [
        ['1', '2', '5'],
        ['1', '3', '6'],
        ['2', '4', '8'],
        ['3', '4', '3'],
    ])
    assert result == 19, f'Wrong answer: {result}'
    result = determine_max_weight(3, [
        ['1', '2', '1'],
        ['1', '2', '2'],
        ['2', '3', '1'],
    ])
    assert result == 3, f'Wrong answer: {result}'
    result = determine_max_weight(5, [
        ['1', '2', '4'],
        ['2', '1', '2'],
    ])
    assert result == 'Oops! I did it again', f'Wrong answer: {result}'
    result = determine_max_weight(2, [])
    assert result == 'Oops! I did it again', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_determine_max_weight()
    count, count_vertex = input().split()
    array = [input().split() for _ in range(int(count_vertex))]
    print(determine_max_weight(int(count), array))
