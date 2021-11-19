def get_hash(ground, module, text):
    if text == '':
        return 0
    index = 0
    result = 0
    size = len(text) - 1
    while index < size:
        result = (((result + ord(text[index])) % module) * ground) % module
        index += 1
    return (result + ord(text[index])) % module


def get_prefixs(ground, module, text, array):
    hashed_text = [get_hash(ground, module, char) for char in text]
    result = []
    for left, right in array:
        result.append(sum(
            hashed_char % module
            for hashed_char in hashed_text[int(left)-1:int(right)]
        ) % module)
    return '\n'.join(str(hashed_text) for hashed_text in result)


def test_get_prefixs():
    result = get_prefixs(1000, 1000009, 'abcdefgh', [
        ['1', '1'],
        ['1', '5'],
        ['2', '3'],
        ['3', '4'],
        ['4', '4'],
        ['1', '8'],
        ['5', '8'],
    ])
    assert result == '97\n225076\n98099\n99100\n100\n436420\n193195', (
        f'Wrong answer: {result}'
    )
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_get_prefixs()
