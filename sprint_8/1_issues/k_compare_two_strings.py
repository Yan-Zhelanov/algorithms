def compare_strings(string_1, string_2):
    left = right = 0
    strings = ['', '']
    change = True
    while change:
        change = False
        if left < len(string_1):
            if ord(string_1[left]) % 2 == 0:
                strings[0] += string_1[left]
            left += 1
            change = True
        if right < len(string_2):
            if ord(string_2[right]) % 2 == 0:
                strings[1] += string_2[right]
            right += 1
            change = True
    return (
        -1 if strings[0] < strings[1]
        else 0 if strings[0] == strings[1]
        else 1
    )


def test_compare_strings():
    result = compare_strings('gggggbbb', 'bbef')
    assert result == -1, f'Wrong answer: {result}'
    result = compare_strings('z', 'aaaaaaa')
    assert result == 1, f'Wrong answer: {result}'
    result = compare_strings('ccccz', 'aaaaaz')
    assert result == 0, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_compare_strings()
    print(compare_strings(input(), input()))
