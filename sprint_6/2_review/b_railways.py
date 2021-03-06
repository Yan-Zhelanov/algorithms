# 63278881

"""
    --- Принцип работы ---
В основе приниципа лежит алгоритм поиска в глубину: мы будем красить вершины
в три цвета, белый — будет нулём, серый — будет единицей, чёрный — будет
двойкой. Граф будем представлять, как ориентированный: дороги одной буквы будут
вести вперёд, а другой буквы будут вести назад. Таким образом, если при обходе
графа в глубину мы наткнёмся на серую вершину, то в графе есть цикл, а значит в
графе есть две разные дороги для двух вершин, в таком случае будем возвращать
значение требуемое условиями задачи.

    --- Доказательство корректности ---
Из описания следует, что если алгоритм поиска в глубину работает корректно, то
и алгоритм будет работать корректно. В данном случае DFS реализован на
массиве, который используется, как стек, в массив будем добавлять все
встречаемые не покрашенные вершины, а после в порядке FIFO будем их посещать и
повторять теже операции для них.

    --- Временная сложность ---
Для каждой вершины запускаем обход в глубину, в лучшем случае уже на второй
итерации мы обнаружим цикл и алгоритм закончит свою работу: O(V - 1). В худшем
случае, мы пройдём по всему графу и не обнаружим цикла: O(V + E).
Итого в худшем и среднем случае: O(V + E)
В лучшем случае: O(V)

    --- Пространственная сложность ---
Нам понадобится хранить цвет для каждой из вершин: O(V), и хранить стек:
O(V - 1)
Итого: O(V + V)
"""

import pathlib

WHITE = 0
GRAY = 1
BLACK = 2

CURRENT_PATH = str(pathlib.Path(__file__).parent.resolve())


def create_graph(count, array):
    graph = [[] for _ in range(count)]
    for index_line in range(count-1):
        for index_char in range(len(array[index_line])):
            if array[index_line][index_char] == 'R':
                graph[index_line].append(index_line+index_char+1)
                continue
            graph[index_line+index_char+1].append(index_line)
    return graph


def is_optimal_map(count, array):
    graph = create_graph(count, array)
    colors = [WHITE] * count
    for current in range(count):
        stack = [current]
        while len(stack) > 0:
            current = stack.pop()
            if colors[current] == WHITE:
                colors[current] = GRAY
                stack.append(current)
                for vertex in graph[current]:
                    if colors[vertex] == WHITE:
                        stack.append(vertex)
                    elif colors[vertex] == GRAY:
                        return False
            elif colors[current] == GRAY:
                colors[current] = BLACK
    return True


def test_is_optimal_map():
    result = is_optimal_map(3, [
        'RR',
        'R',
    ])
    assert result, f'Wrong answer: {result}'
    result = is_optimal_map(3, [
        'RR',
        'B',
    ])
    assert result, f'Wrong answer: {result}'
    result = is_optimal_map(3, [
        'RB',
        'R',
    ])
    assert not result, f'Wrong answer: {result}'
    result = is_optimal_map(3, [
        'BR',
        'R',
    ])
    assert result, f'Wrong answer: {result}'
    result = is_optimal_map(4, [
        'RBR',
        'RR',
        'R',
    ])
    assert not result, f'Wrong answer: {result}'
    result = is_optimal_map(4, [
        'RRR',
        'BR',
        'R',
    ])
    assert result, f'Wrong answer: {result}'
    result = is_optimal_map(4, [
        'RRR',
        'RB',
        'R',
    ])
    assert not result, f'Wrong answer: {result}'
    result = is_optimal_map(4, [
        'BBB',
        'RB',
        'B',
    ])
    assert result, f'Wrong answer: {result}'
    result = is_optimal_map(5, [
        'RRRB',
        'BRR',
        'BR',
        'R',
    ])
    assert not result, f'Wrong answer: {result}'
    result = is_optimal_map(5, [
        'RBRR',
        'RBR',
        'RB',
        'R',
    ])
    assert not result, f'Wrong answer: {result}'
    result = is_optimal_map(5, [
        'BRBR',
        'BBR',
        'BB',
        'R',
    ])
    assert not result, f'Wrong answer: {result}'
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
    assert result, f'Wrong answer: {result}'
    print('All tests passed!')


def test_speed_is_optimal_map():
    with open(CURRENT_PATH + '/input.txt', 'r') as array:
        array = [line[:-2] for line in array]
        is_optimal_map(len(array), array)


def create_output_for_test():
    from random import choice
    count = 100
    text = (
        '\n'.join([
            ''.join(choice('RB') for _ in range(count-index-1))
            for index in range(count-1)
        ])
    )
    with open(CURRENT_PATH + '/input.txt', 'w') as output:
        output.writelines(text)


if __name__ == '__main__':
    # test_is_optimal_map()
    # create_output_for_test()
    # test_speed_is_optimal_map()
    count = int(input())
    array = [input() for _ in range(count-1)]
    if is_optimal_map(count, array):
        print('YES')
    else:
        print('NO')
