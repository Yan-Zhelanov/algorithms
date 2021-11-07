def determine_max_rounds_draw(rounds):
    pass


def test_determine_max_rounds_draw():
    result = determine_max_rounds_draw('0 1')
    assert result == 2, f'Wrong answer: {result}'
    result = determine_max_rounds_draw('0 1 0')
    assert result == 2, f'Wrong answer: {result}'
    result = determine_max_rounds_draw('0 0 1 0 1 1 1 0 0 0')
    assert result == 8, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_determine_max_rounds_draw()
