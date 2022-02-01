# @profile
def get_fibonacci_last_numbers(number, count_last):
    first = 0
    second = 1
    result = 1
    index = 0
    module = 10 ** count_last
    while index < number:
        result = (first + second) % module
        first = second
        second = result
        index += 1
    return result


def test_get_fibonacci_last_numbers():
    result = get_fibonacci_last_numbers(0, 5)
    assert result == 1, f'Wrong answer: {result}'
    result = get_fibonacci_last_numbers(3, 1)
    assert result == 3, f'Wrong answer: {result}'
    result = get_fibonacci_last_numbers(10, 1)
    assert result == 9, f'Wrong answer: {result}'
    result = get_fibonacci_last_numbers(11, 1)
    assert result == 4, f'Wrong answer: {result}'
    result = get_fibonacci_last_numbers(11, 5)
    assert result == 144, f'Wrong answer: {result}'
    result = get_fibonacci_last_numbers(21, 5)
    assert result == 17711, f'Wrong answer: {result}'
    result = get_fibonacci_last_numbers(21, 4)
    assert result == 7711, f'Wrong answer: {result}'
    result = get_fibonacci_last_numbers(484, 2)
    assert result == 85, f'Wrong answer: {result}'
    result = get_fibonacci_last_numbers(506277, 6)
    assert result == 263439, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_get_fibonacci_last_numbers()
    print(get_fibonacci_last_numbers(*map(int, input().split())))
