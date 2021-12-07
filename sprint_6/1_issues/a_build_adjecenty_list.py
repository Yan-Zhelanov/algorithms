def get_adjecenty_list(array):
    result = []
    for line in array:
        vertex, to = int(line[0]), int(line[1])
        while vertex-1 > len(result)-1:
            result.append(0)
        if result[vertex-1] == 0:
            result[vertex-1] = [1, to]
            continue
        result[vertex-1][0] += 1
        result[vertex-1].append(to)
    return '\n'.join(
        ' '.join(str(num) for num in line)
        if line != 0
        else '0'
        for line in result
    )


def test_get_adjecenty_list():
    result = get_adjecenty_list([
        ['1', '3'],
        ['2', '3'],
        ['5', '2'],
    ])
    assert result == '1 3\n1 3\n0\n0\n1 2', f'Wrong answer: {result}'
    result = get_adjecenty_list([
        ['1', '2'],
    ])
    assert result == '1 2', f'Wrong answer: {result}'
    result = get_adjecenty_list([
        ['1', '2'],
        ['1', '3'],
        ['1', '4']
    ])
    assert result == '3 2 3 4', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_get_adjecenty_list()
    _, count = input().split()
    array = [input().split() for _ in range(int(count))]
    print(get_adjecenty_list(array))
