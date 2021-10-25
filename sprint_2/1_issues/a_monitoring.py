def rotate(y, x, array):
    result = [[''] * y for _ in range(x)]
    for index_y in range(y):
        for index_x in range(x):
            result[index_x][index_y] = array[index_y][index_x]
    return '\n'.join(' '.join(row) for row in result)


def test_rotate():
    result = rotate(4, 3, [
        ['1', '2', '3'],
        ['0', '2', '6'],
        ['7', '4', '1'],
        ['2', '7', '0'],
    ])
    assert result == '1 0 7 2\n2 2 4 7\n3 6 1 0', f'Wrong answer: {result}'
    result = rotate(2, 2, [
        ['-1', '2'],
        ['-99', '0'],
    ])
    assert result == '-1 -99\n2 0', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_rotate()
    y, x = int(input()), int(input())
    array = [input().split() for _ in range(y)]
    print(rotate(y, x, array))
