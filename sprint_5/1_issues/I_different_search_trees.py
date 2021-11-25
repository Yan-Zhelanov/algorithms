def determine_count_trees(count):
    result = count
    count -= 1
    while count > 0:
        pass
    return result


def test_determine_count_trees():
    result = determine_count_trees(1)
    assert result == 1, f'Wrong answer: {result}'
    result = determine_count_trees(2)
    assert result == 2, f'Wrong answer: {result}'
    result = determine_count_trees(3)
    assert result == 5, f'Wrong answer: {result}'
    result = determine_count_trees(4)
    assert result == 14, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_determine_count_trees()
