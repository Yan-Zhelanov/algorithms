def determine_extra_char(word, word_extra):
    word_extra = list(word_extra)
    for char in word:
        word_extra.pop(word_extra.index(char))
    return word_extra[0]


def test_determine_extra_char():
    result = determine_extra_char('abcd', 'abcde')
    assert result == 'e', f'Wrong answer: {result}'
    result = determine_extra_char('og', 'ogg')
    assert result == 'g', f'Wrong answer: {result}'
    result = determine_extra_char('xtkpx', 'xkctpx')
    assert result == 'c', f'Wrong answer: {result}'
    result = determine_extra_char('xxx', 'xxxx')
    assert result == 'x', f'Wrong answer: {result}'
    result = determine_extra_char('abba', 'baaba')
    assert result == 'a', f'Wrong answer: {result}'
    result = determine_extra_char('a', 'ax')
    assert result == 'x', f'Wrong answer: {result}'
    result = determine_extra_char('lililililililo', 'liililililililo')
    assert result == 'i', f'Wrong answer: {result}'
    result = determine_extra_char('xaqwertyu', 'uxaqwertyu')
    assert result == 'u', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_extra_char()
    print(determine_extra_char(input(), input()))
