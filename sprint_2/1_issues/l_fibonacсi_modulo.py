from math import fsum, pow


def get_fibonacci_last_nums(num, count_last):
    num += 1
    left = pow(((1 + pow(5, 0.5)) / 2), num)
    right = -pow(((1 - pow(5, 0.5)) / 2), num)
    result = (
        fsum([left, right])
        / pow(5, 0.5)
    ) % pow(10, count_last)
    return f'{result:.0f}'


def test_get_fibonacci_last_nums():
    result = get_fibonacci_last_nums(3, 1)
    assert result == '3', f'Wrong answer: {result}'
    result = get_fibonacci_last_nums(10, 1)
    assert result == '9', f'Wrong answer: {result}'
    result = get_fibonacci_last_nums(11, 1)
    assert result == '4', f'Wrong answer: {result}'
    result = get_fibonacci_last_nums(11, 5)
    assert result == '144', f'Wrong answer: {result}'
    result = get_fibonacci_last_nums(21, 5)
    assert result == '17711', f'Wrong answer: {result}'
    result = get_fibonacci_last_nums(21, 4)
    assert result == '7711', f'Wrong answer: {result}'
    result = get_fibonacci_last_nums(484, 2)
    assert result == '85', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_get_fibonacci_last_nums()
    print(get_fibonacci_last_nums(*map(int, input().split())))
