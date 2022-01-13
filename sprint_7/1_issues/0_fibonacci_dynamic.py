def get_fibonacci(num):
    if num == 1:
        return 1
    first = 0
    second = 1
    current = 0
    index = 1
    while index < num:
        current = first + second
        first = second
        second = current
        index += 1
    return current


def test_get_fibonacci():
    result = get_fibonacci(3)
    assert result == 2, f'Wrong answer: {result}'
    result = get_fibonacci(4)
    assert result == 3, f'Wrong answer: {result}'
    result = get_fibonacci(5)
    assert result == 5, f'Wrong answer: {result}'
    result = get_fibonacci(6)
    assert result == 8, f'Wrong answer: {result}'
    result = get_fibonacci(0)
    assert result == 0, f'Wrong answer: {result}'
    result = get_fibonacci(1)
    assert result == 1, f'Wrong answer: {result}'
    result = get_fibonacci(2)
    assert result == 1, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_get_fibonacci()
