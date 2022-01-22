def get_reversed(text):
    text = text.split()
    result = []
    for word in reversed(text):
        result.append(word)
    return ' '.join(result)


def test_get_reversed():
    result = get_reversed('i am crazy')
    assert result == 'crazy am i', f'Wrong answer: {result}'
    result = get_reversed('lazy')
    assert result == 'lazy', f'Wrong answer: {result}'
    result = get_reversed('a b c')
    assert result == 'c b a', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_get_reversed()
    print(get_reversed(input()))
