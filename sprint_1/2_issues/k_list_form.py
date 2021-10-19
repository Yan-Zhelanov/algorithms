def get_sum_list_form(a, b):
    a = int(a.replace(' ', ''))
    result = str(a + b)
    return ' '.join(result)


def test_get_sum_list_form():
    result = get_sum_list_form('1 2 0 0', 34)
    assert result == '1 2 3 4', f'Wrong answer: {result}'
    result = get_sum_list_form('9 5', 17)
    assert result == '1 1 2', f'Wrong answer: {result}'
    result = get_sum_list_form('1', 10)
    assert result == '1 1', f'Wrong answer: {result}'
    result = get_sum_list_form('0', 0)
    assert result == '0', f'Wrong answer: {result}'
    result = get_sum_list_form('1', 0)
    assert result == '1', f'Wrong answer: {result}'
    result = get_sum_list_form('0', 1)
    assert result == '1', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_get_sum_list_form()
    input()
    print(get_sum_list_form(input(), int(input())))
