def determine_neighbors(max_x, max_y, array, x, y):
    neighbors = []
    if x - 1 >= 0:
        neighbors.append(array[x-1][y])
    if x + 1 < max_x:
        neighbors.append(array[x+1][y])
    if y - 1 >= 0:
        neighbors.append(array[x][y-1])
    if y + 1 < max_y:
        neighbors.append(array[x][y+1])
    return ' '.join(map(str, sorted(neighbors)))


def test_determine_neighbors():
    result = determine_neighbors(
        4, 3,
        [
            [1, 2, 3],
            [0, 2, 6],
            [7, 4, 1],
            [2, 7, 0],
        ],
        3, 0
    )
    assert result == '7 7', f'Wrong result: {result}'
    result = determine_neighbors(
        4, 3,
        [
            [1, 2, 3],
            [0, 2, 6],
            [7, 4, 1],
            [2, 7, 0],
        ],
        0, 0
    )
    assert result == '0 2'
    result = determine_neighbors(
        4, 3,
        [
            [1, 2, 3],
            [0, 2, 6],
            [7, 4, 1],
            [2, 7, 0],
        ],
        2, 1
    )
    assert result == '1 2 7 7'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    max_x, max_y = int(input()), int(input())
    array = [list(map(int, input().split())) for _ in range(max_x)]
    print(determine_neighbors(
        max_x, max_y, array, int(input()), int(input())
    ))
