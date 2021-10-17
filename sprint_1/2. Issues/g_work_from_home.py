def get_binary_number(number):
    result = ''
    while number >= 2:
        result += str(number % 2)
        number //= 2
    result += '1'
    return int(''.join(
        result[index] for index in range(len(result)-1, -1, -1)
    ))


def test_get_binary_number():
    result = get_binary_number(5)
    assert result == 101, f'Wrong answer: {result}'
    result = get_binary_number(14)
    assert result == 1110, f'Wrong answer: {result}'
    result = get_binary_number(256)
    assert result == 100000000, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    print(get_binary_number(int(input())))
