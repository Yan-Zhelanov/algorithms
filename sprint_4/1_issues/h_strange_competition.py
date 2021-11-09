def is_equal(text_1, text_2):
    if len(text_1) != len(text_2):
        return 'NO'
    charaters = {}
    for char_1, char_2 in zip(text_1, text_2):
        if charaters.get(char_1, None) is None:
            if char_2 not in charaters.values():
                charaters[char_1] = char_2
            else:
                return 'NO'
        if charaters[char_1] != char_2:
            return 'NO'
    return 'YES'


def test_is_equal():
    result = is_equal('mxyskaoghi', 'qodfrgmslc')
    assert result == 'YES'
    result = is_equal('aaaadddd', 'xxxxeeee')
    assert result == 'YES'
    result = is_equal('a', 'd')
    assert result == 'YES'
    result = is_equal('aaaaa', 'dddde')
    assert result == 'NO'
    result = is_equal('aba', 'xxx')
    assert result == 'NO'
    result = is_equal('abbb', 'abbbb')
    assert result == 'NO'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_is_equal()
    print(is_equal(input(), input()))
