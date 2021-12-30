# 63257704

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
В начале мы создаём списки смежности: O(V + E), где V — количество вершин, а
E — количество рёбер. После мы для каждой вершины запускаем обход в глубину, в
лучшем случае уже на второй итерации мы обнаружим цикл и алгоритм закончит свою
работу: O(V-1). В худшем случае, мы пройдём по всему графу и не обнаружим
цикла: O(V + E).
Итого в худшем и среднем случае: O(V + E + V + E)
В лучшем случае: O(V + E + V)

    --- Пространственная сложность ---
Нам понадобится хранить списки смежностей: O(V + E), также нам понадобится
хранить цвет для каждой из вершин: O(V), и хранить стек: O(V-1)
Итого: O(V + E + V + V)
"""


def is_optimal_map(count, array):
    graph = [[] for _ in range(count)]
    for index_line in range(count-1):
        for index_char in range(len(array[index_line])):
            if array[index_line][index_char] == 'R':
                graph[index_line].append(index_line+index_char+1)
                continue
            graph[index_line+index_char+1].append(index_line)
    colors = [0] * count
    for current in range(count):
        stack = [current]
        while len(stack) > 0:
            current = stack.pop()
            if colors[current] == 0:
                colors[current] = 1
                stack.append(current)
                for vertex in graph[current]:
                    if colors[vertex] == 0:
                        stack.append(vertex)
                    elif colors[vertex] == 1:
                        return 'NO'
            elif colors[current] == 1:
                colors[current] = 2
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


# def test_speed_is_optimal_map():
#     with open('output.txt', 'r') as array:
#         array = [line[:-2] for line in array]
#         is_optimal_map(array)


# def create_output_for_test():
#     from random import choice
#     count = 3000
#     text = (
#         '\n'.join([
#             ''.join(choice('RB') for _ in range(count-index-1))
#             for index in range(count-1)
#         ])
#     )
#     with open('output.txt', 'w') as output:
#         output.writelines(text)


if __name__ == '__main__':
    # test_is_optimal_map()
    # create_output_for_test()
    # test_speed_is_optimal_map()
    count = int(input())
    array = [input() for _ in range(count-1)]
    print(is_optimal_map(count, array))
