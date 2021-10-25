def get_fibonachi(num):
    if num == 0 or num == 1:
        return 1
    return get_fibonachi(num-2) + get_fibonachi(num-1)


def test_get_fibonachi():
    result = get_fibonachi(0)
    assert result == 1, f'Wrong answer: {result}'
    result = get_fibonachi(1)
    assert result == 1, f'Wrong answer: {result}'
    result = get_fibonachi(2)
    assert result == 2, f'Wrong answer: {result}'
    result = get_fibonachi(3)
    assert result == 3, f'Wrong answer: {result}'
    result = get_fibonachi(4)
    assert result == 5, f'Wrong answer: {result}'
    result = get_fibonachi(5)
    assert result == 8, f'Wrong answer: {result}'
    result = get_fibonachi(11)
    assert result == 144, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_get_fibonachi()
    print(get_fibonachi(int(input())))
