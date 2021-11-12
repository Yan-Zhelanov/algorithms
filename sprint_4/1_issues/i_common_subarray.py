def determine_max_area(array_1, array_2):
    pass


def test_determine_max_area():
    result = determine_max_area([1, 2, 3, 2, 1], [3, 2, 1, 5, 6])
    assert result == 3, f'Wrong answer: {result}'
    result = determine_max_area([1, 2, 3, 2, 1], [5, 6, 1, 2])
    assert result == 2, f'Wrong answer: {result}'
    result = determine_max_area([1, 2, 3, 2, 1, 5, 6], [5, 6, 1, 2])
    assert result == 4, f'Wrong answer: {result}'
    result = determine_max_area([1, 2, 4, 5, 3, 2], [5, 6, 3, 1, 2, 3, 1])
    assert result == 5, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_determine_max_area()
