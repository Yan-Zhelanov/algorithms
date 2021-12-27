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
    colors = [0] * count
    stack = []
    length = count - 1
    for current in range(length):
        if colors[current] != 0:
            continue
        stack.append(current)
        while len(stack) != 0:
            current = stack.pop()
            if colors[current] == 1:
                colors[current] = 2
                continue
            colors[current] = 1
            stack.append(current)
            for vertex in range(current-1, -1, -1):
                index_current = current - vertex - 1
                if array[vertex][index_current] == 'B' or colors[vertex] == 2:
                    continue
                if colors[vertex] == 1:
                    return 'NO'
                stack.append(vertex)
            if current == length:
                continue
            for index_vertex in range(len(array[current])):
                vertex = current + index_vertex + 1
                if array[current][index_vertex] == 'R' or colors[vertex] == 2:
                    continue
                if colors[vertex] == 1:
                    return 'NO'
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
