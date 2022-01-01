# 63278661

"""
    --- Принцип работы ---
Граф будем хранить в виде списка словарей смежности: индексом будет вершина,
ключами будут смежные ей вершины, а в значениях будут лежать веса. Если у двух
вершин есть кратные рёбра, то будем записывать вес бо́льшего ребра. Посещённые
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
проверять все смежные ей вершины: O(E).
Итого в худшем, среднем и лучшем случаях: O(E + E)

    --- Пространственная сложность ---
Мы будем хранить множество уже посещённых вершин, по началу оно будет пусто,
но под конец будет полностью заполнено: O(V), а ещё мы будем хранить ребра,
которые мы можем посетить в текущий момент: O(E * 3). В лучшем случае мы будем
хранить всегда только одно ребро: O(1 * 3).
Итого в худшем и среднем случаях: O(V + E)
В лучшем случае: O(V)
"""


from heapq import heappush, heappop

CONNECTIVITY_ERROR = 'Oops! I did it again'


def create_graph(count, edges):
    graph = [{} for _ in range(count)]
    for edge in edges:
        if len(edge) != 3:
            continue
        left, right, weight = int(edge[0])-1, int(edge[1])-1, int(edge[2])
        if graph[left].get(right, 0) >= weight:
            continue
        graph[left][right] = weight
        graph[right][left] = weight
    return graph


def determine_max_weight(count, array, connectivity_error=CONNECTIVITY_ERROR):
    def _bypass_one_vertex(current, edges, visited):
        visited.add(current)
        for vertex in graph[current]:
            if vertex not in visited:
                heappush(edges, [-graph[current][vertex], current, vertex])

    if count == 1:
        return 0
    if len(array) == 0:
        return connectivity_error
    edges = []
    max_weight = 0
    visited = set()
    graph = create_graph(count, array)
    current = list(graph[0].keys())[0]
    while len(visited) != count:
        _bypass_one_vertex(current, edges, visited)
        if len(edges) == 0 or len(visited) == count:
            break
        current = heappop(edges)
        while current[2] in visited:
            if len(edges) == 0:
                return connectivity_error
            current = heappop(edges)
        max_weight += -current[0]
        current = current[2]
    if len(visited) != count:
        return connectivity_error
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
    assert result == CONNECTIVITY_ERROR, f'Wrong answer: {result}'
    result = determine_max_weight(2, [])
    assert result == CONNECTIVITY_ERROR, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_determine_max_weight()
    count, count_edges = input().split()
    array = [input().split() for _ in range(int(count_edges))]
    print(determine_max_weight(int(count), array))
