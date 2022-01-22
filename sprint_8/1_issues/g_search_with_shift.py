def find_pattern_positions(temperatures, pattern, start=0):
    if len(temperatures) == 0 or len(pattern) == 0:
        return ''
    temperatures = list(map(int, temperatures))
    pattern = list(map(int, pattern))
    positions = []
    for position in range(start, len(temperatures)-len(pattern)+1):
        match = True
        for offset in range(1, len(pattern)):
            if temperatures[position+offset]-temperatures[position+offset-1] != pattern[offset]-pattern[offset-1]:
                match = False
                break
        if match:
            positions.append(position+1)
    return ' '.join(str(position) for position in positions)


def test_find_pattern_positions():
    result = find_pattern_positions(
        ['1', '3', '4', '5'],
        ['3', '4'],
    )
    assert result == '2 3', f'Wrong answer: {result}'
    result = find_pattern_positions(
        ['3', '9', '1', '2', '5', '10', '9', '1', '7'],
        ['4', '10'],
    )
    assert result == '1 8', f'Wrong answer: {result}'
    result = find_pattern_positions(
        [],
        [],
    )
    assert result == '', f'Wrong answer: {result}'
    result = find_pattern_positions(
        ['1', '2', '3', '4', '5'],
        ['1', '2', '3'],
    )
    assert result == '1 2 3', f'Wrong answer: {result}'
    result = find_pattern_positions(
        ['1', '10', '33', '55'],
        ['2', '11', '34'],
    )
    assert result == '1', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_find_pattern_positions()
    input()
    temperatures = input().split()
    input()
    print(find_pattern_positions(temperatures, input().split()))
