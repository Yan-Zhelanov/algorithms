def determine_groups(array):
    groups = {}
    for index, item in enumerate(array):
        item = ''.join(sorted(item))
        groups[item] = groups.get(item, []) + [index]
    return '\n'.join(' '.join(
        str(item) for item in line
    ) for line in sorted(groups.values()))


def test_determine_groups():
    result = determine_groups(['tan', 'eat', 'tea', 'ate', 'nat', 'bat'])
    assert result == '0 4\n1 2 3\n5', f'Wrong answer: {result}'
    result = determine_groups(['ttt', 'kukold', 'easy', 'late', 'ffff'])
    assert result == '0\n1\n2\n3\n4', f'Wrong answer: {result}'
    result = determine_groups([
        'ttt', 'kukold', 'easy', 'ysea', 'ldokuk', 'ttt'
    ])
    assert result == '0 5\n1 4\n2 3', f'Wrong answer: {result}'
    result = determine_groups([
        'lamdba', 'aamdbl', 'almdab', 'amadlb', 'dablma', 'badalm'
    ])
    assert result == '0 1 2 3 4 5', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_groups()
    input()
    print(determine_groups(input().split()))
