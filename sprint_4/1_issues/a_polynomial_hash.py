def get_hash(ground, module, text):
    if text == '':
        return 0
    index = 0
    result = 0
    size = len(text) - 1
    while index < size:
        result = (((result + ord(text[index])) % module) * ground) % module
        index += 1
    result = (result + ord(text[index])) % module
    return result


def test_get_hash():
    result = get_hash(123, 100003, 'HaSH')
    assert result == 56156, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_get_hash()
    print(get_hash(int(input()), int(input()), input()))
