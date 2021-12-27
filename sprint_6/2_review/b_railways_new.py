"""
    --- Принцип работы ---
В основе приниципа лежит алгоритм поиска в глубину: мы будем красить вершины
в три цвета, белый — будет нулём, серый — будет единицей, чёрный — будет
двойкой. Граф будет представлять, как ориентированный: дороги одной буквы будут
вести вперёд, а другой буквы будут вести назад. Таким образом, если при обходе
графа в глубину мы наткнёмся на серую вершину, то в графе есть цикл, а значит в
графе есть две разные дороги для двух вершин, в таком случае будем возвращать
значение требуемое условиями задачи.

    --- Доказательство корректности ---
Из описания следует, что если алгоритм поиска в глубину работает корректно, то
и алгоритм будет работать корректно. В данном случае алгоритм реализован на
массиве, в массив будем добавлять все встречаемые нам вершины,

    --- Временная сложность ---


    --- Пространственная сложность ---

"""


def is_optimal_map(count, array):
    graph = [[] for _ in range(count)]
    for vertex in range(count-1):
        for index_route in range(len(array[vertex])):
            if array[vertex][index_route] == 'R':
                graph[vertex].append(vertex+index_route+1)
                continue
            graph[vertex+index_route+1].append(vertex)
    colors = [0] * count
    for current in range(count):
        if colors[current] == 2:
            continue
        stack = [current]
        while len(stack) != 0:
            current = stack.pop()
            if colors[current] == 1:
                colors[current] = 2
                continue
            colors[current] = 1
            stack.append(current)
            for vertex in graph[current]:
                if colors[vertex] == 1:
                    return 'NO'
                if colors[vertex] == 0:
                    stack.append(vertex)
    return 'YES'


def test_is_optimal_map():
    result = is_optimal_map(3, [
        'RR',
        'R',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map(3, [
        'RR',
        'B',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map(3, [
        'RB',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map(3, [
        'BR',
        'R',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map(4, [
        'RBR',
        'RR',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map(4, [
        'RRR',
        'BR',
        'R',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map(4, [
        'RRR',
        'RB',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map(4, [
        'BBB',
        'RB',
        'B',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    result = is_optimal_map(5, [
        'RRRB',
        'BRR',
        'BR',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map(5, [
        'RBRR',
        'RBR',
        'RB',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map(5, [
        'BRBR',
        'BBR',
        'BB',
        'R',
    ])
    assert result == 'NO', f'Wrong answer: {result}'
    result = is_optimal_map(10, [
        'RRBRRBRRR',
        'BBBBBBRB',
        'BBRBRRR',
        'RRBRRR',
        'RBRRR',
        'BBRR',
        'RRR',
        'RR',
        'B',
    ])
    assert result == 'YES', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_is_optimal_map()
    count = int(input())
    array = [input() for _ in range(count-1)]
    print(is_optimal_map(count, array))
