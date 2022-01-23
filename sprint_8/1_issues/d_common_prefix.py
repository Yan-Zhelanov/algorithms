def determine_max_common_prefix(strings):
    result = 0
    for i in range(len(min(strings, key=len))):
        symbol = strings[0][i]
        for string in strings[1:]:
            if string[i] != symbol:
                return result
        result += 1
    return result

def test_determine_max_common_prefix():
    result = determine_max_common_prefix([
        'abcd',
        'abeee',
        'abssss',
    ])
    assert result == 2, f'Wrong answer: {result}'
    result = determine_max_common_prefix([
        'customer',
        'custoder',
    ])
    assert result == 5, f'Wrong answer: {result}'
    result = determine_max_common_prefix([
        'keker',
    ])
    assert result == 5, f'Wrong answer: {result}'
    result = determine_max_common_prefix([
        'keker',
        '',
    ])
    assert result == 0, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_determine_max_common_prefix()
    strings = [input() for _ in range(int(input()))]
    print(determine_max_common_prefix(strings))
