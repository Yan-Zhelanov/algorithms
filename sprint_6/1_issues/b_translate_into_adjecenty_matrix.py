def get_adjecenty_matrix(count, array):
    result = [[0] * count for _ in range(count)]
    for line in array:
        result[int(line[0])-1][int(line[1])-1] = 1
    return '\n'.join(' '.join(str(num) for num in line) for line in result)


def test_get_adjecenty_matrix():
    result = get_adjecenty_matrix(5, [
        ['1', '3'],
        ['2', '3'],
        ['5', '2'],
    ])
    assert result == '0 0 1 0 0\n0 0 1 0 0\n0 0 0 0 0\n0 0 0 0 0\n0 1 0 0 0', (
        f'Wrong answer: {result}'
    )
    result = get_adjecenty_matrix(2, [
        ['1', '2'],
    ])
    assert result == '0 1\n0 0', (
        f'Wrong answer: {result}'
    )
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_get_adjecenty_matrix()
    count, count_edges = input().split()
    array = [input().split() for _ in range(int(count_edges))]
    print(get_adjecenty_matrix(int(count), array))
