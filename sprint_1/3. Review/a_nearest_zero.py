def determine_nearest_zeros(array):
    pass


def test_determine_nearest_zeros():
    result = determine_nearest_zeros('0 1 4 9 0')
    assert result == '0 1 2 1 0', f'Wrong answer: {result}'
    result = determine_nearest_zeros('0 7 9 4 8 20')
    assert result == '0 1 2 3 4 5', f'Wrong answer: {result}'
    result = determine_nearest_zeros('1 7 9 4 8 20 0')
    assert result == '6 5 4 3 2 1 0', f'Wrong answer: {result}'
    result = determine_nearest_zeros('1 7 9 4 8 20 0 1')
    assert result == '6 5 4 3 2 1 0 1', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_determine_nearest_zeros()
