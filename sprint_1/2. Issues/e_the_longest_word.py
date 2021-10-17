def get_longest_word(words):
    max_word = ''
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return f'{max_word}\n{len(max_word)}'


def test_get_longest_word():
    result = get_longest_word(['i', 'love', 'segment', 'tree'])
    assert result == 'segment\n7'
    result = get_longest_word(['frog', 'jumps', 'from', 'river'])
    assert result == 'jumps\n5'
    result = get_longest_word(['i', '2', 'l', 'q'])
    assert result == 'i\n1'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    input()
    print(get_longest_word(input().split()))
