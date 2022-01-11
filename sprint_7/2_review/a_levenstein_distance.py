def determine_levenstein_distance(string_1, string_2):
    pass


def test_determine_levenstein_distance():
    result = determine_levenstein_distance('queue', 'ueue')
    assert result == 1, f'Wrong answer: {result}'
    result = determine_levenstein_distance('abacaba', 'abaabc')
    assert result == 2, f'Wrong answer: {result}'
    result = determine_levenstein_distance('innokentiy', 'innnokkentia')
    assert result == 3, f'Wrong answer: {result}'
    result = determine_levenstein_distance('r', 'x')
    assert result == 1, f'Wrong answer: {result}'
    result = determine_levenstein_distance('q', 'q')
    assert result == 0, f'Wrong answer: {result}'
    result = determine_levenstein_distance('', 'x')
    assert result == 1, f'Wrong answer: {result}'
    result = determine_levenstein_distance('', '')
    assert result == 0, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_determine_levenstein_distance()
