# 62414290

"""
    --- Принцип работы ---
Граф будем хранить в виде списка словарей смежности: индексом будет вершина,
ключами будут смежные ей вершины, а в значениях будут лежать веса. Если у двух
вершин есть кратные рёбра, то будем записывать вес большего ребра. Посещённые
вершины будем добавлять в множество, а рёбра, которые мы можем посетить будем
хранить в куче минимума, где вес вершин будем ставить на первое место в
массиве, при этом добавляя к нему знак отрицания, тем самым в корне кучи будет
лежать не минимальный элемент, а максимальный. Выберем любую вершину, добавим
все рёбра смежных ей и одновременно непосещённых вершин. Если количество вершин
после добавления равняется нулю, значит перед нами несвязный граф, вернём
соответствующий ответ. Если количество посещённых вершин равняется общему
количеству вершин, значит мы посетили все возможные вершины и можем закончить
обход. В противном случае, будем доставать из кучи самые большие ребра, до тех
пор пока конечная вершина ребра не будет в множестве посещённых вершин или
рёбра не закончатся. Прибавим вес найденного ребра к нашему ответу и повторим
все действия для конечной вершины.

    --- Доказательство корректности ---
Из описания следует, что каждую итерацию мы будем выбирать самое большое ребро
из рёбер уже посещённых вершин, таким образом мы будем использовать только
самые "тяжёлые" ребра, которые сформируют максимальное остовное дерево, если
граф связный.

    --- Временная сложность ---
Чтобы записать граф в виде списка смежности нам понадобится O(E) времени, где
E — количество рёбер в графе. Далее мы пройдёмся по каждой вершине и будем
проверять все смежные ей вершины, в худшем случае, если из каждой вершины можно
добраться во все остальные вершины: O(V * V-1), где V — количество вершин в
графе. В лучшем случае, из каждой вершины можно добраться только в одну
вершину, тогда сложность будет: O(V * 1)
Итого в худшем: O(E + V^2)
В среднем: O(E + V^2)
В лучшем: O(E + V)

    --- Пространственная сложность ---
Мы будем хранить список смежностей: O(V + E), также мы будем хранить множество
уже посещённых вершин, по началу оно будет пусто, но под конец будет полностью
заполнено: O(V), а ещё мы будем хранить ребра, которые мы можем посетить в
текущий момент: O(E * 3). В лучшем случае мы будем хранить всегда только одно
ребро: O(1 * 3).
Итого в худшем: O(V + E + V + E)
В среднем: O(V + E + V + E)
В лучшем: O(V + E + V)
"""


from heapq import heappush, heappop


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
    edges = []
    max_weight = 0
    current = list(graph[0].keys())[0]
    while len(visited) != count:
        visited.add(current)
        for vertex in graph[current]:
            if vertex in visited:
                continue
            heappush(edges, [-graph[current][vertex], current, vertex])
        if len(edges) == 0 or len(visited) == count:
            break
        while True:
            current = heappop(edges)
            if current[2] in visited:
                if len(edges) == 0:
                    return 'Oops! I did it again'
                continue
            break
        max_weight += -current[0]
        current = current[2]
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
