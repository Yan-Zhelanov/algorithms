def is_degree_of(number, root=4):
    if number == 1 or number == root:
        return True
    value = root
    while value <= number:
        value *= root
        if value == number:
            return True
    return False


def test_is_degree_of():
    result = is_degree_of(15)
    assert result == False, f'Wrong answer: {result}'
    result = is_degree_of(16)
    assert result == True, f'Wrong answer: {result}'
    result = is_degree_of(32)
    assert result == False, f'Wrong answer: {result}'
    result = is_degree_of(1)
    assert result == True, f'Wrong answer: {result}'
    result = is_degree_of(1555)
    assert result == False, f'Wrong answer: {result}'
    result = is_degree_of(1024)
    assert result == True, f'Wrong answer: {result}'
    result = is_degree_of(4)
    assert result == True, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_is_degree_of()
    # print(is_degree_of(int(input())))
