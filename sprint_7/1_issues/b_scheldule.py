def determine_max_lessons(array):
    for index in range(len(array)):
        array[index] = [float(array[index][0]), float(array[index][1])]
    array.sort(key=lambda line: (line[1], line[0]))
    result = [array[0]]
    for index in range(1, len(array)):
        if result[-1][1] <= array[index][0]:
            result.append(array[index])
    return f'{len(result)}\n' + '\n'.join(
        ' '.join(f'{num:g}' for num in line)
        for line in result
    )


def test_determine_max_lessions():
    result = determine_max_lessons([
        ['9', '10'],
        ['9.3', '10.3'],
        ['10', '11'],
        ['10.3', '11.3'],
        ['11', '12'],
    ])
    assert result == '3\n9 10\n10 11\n11 12', f'Wrong answer: {result}'
    result = determine_max_lessons([
        ['9', '10'],
        ['11', '12.25'],
        ['12.15', '13.3'],
    ])
    assert result == '2\n9 10\n11 12.25', f'Wrong answer: {result}'
    result = determine_max_lessons([
        ['19', '19'],
        ['7', '14'],
        ['12', '14'],
        ['8', '22'],
        ['22', '23'],
        ['5', '21'],
        ['9', '23'],
    ])
    assert result == '3\n7 14\n19 19\n22 23', f'Wrong answer: {result}'
    result = determine_max_lessons([
        ['19', '19'],
        ['0', '0'],
        ['1', '2'],
        ['2', '2'],
        ['2', '3'],
        ['3', '3'],
        ['3', '6'],
        ['1', '4'],
        ['1', '4'],
    ])
    assert result == '7\n0 0\n1 2\n2 2\n2 3\n3 3\n3 6\n19 19', (
        f'Wrong answer: {result}'
    )
    print('All tests passed!')


if __name__ == '__main__':
    # test_determine_max_lessions()
    count = int(input())
    array = [input().split() for _ in range(count)]
    print(determine_max_lessons(array))
