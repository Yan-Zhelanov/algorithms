# 55424928
OPERATIONS = {
    '+': lambda num_1, num_2: num_1 + num_2,
    '-': lambda num_1, num_2: num_1 - num_2,
    '*': lambda num_1, num_2: num_1 * num_2,
    '/': lambda num_1, num_2: num_1 // num_2,
}


def calculate(array):
    result = []
    for item in array:
        if item in '+-/*':
            result.append(
                OPERATIONS[item](num_2=result.pop(), num_1=result.pop())
            )
            continue
        result.append(int(item))
    return result[-1]


def test_calculate():
    result = calculate(['2', '1', '+', '3', '*'])
    assert result == 9, f'Wrong answer: {result}'
    result = calculate(['9', '3', '/', '3', '-'])
    assert result == 0, f'Wrong answer: {result}'
    result = calculate(['12', '5', '/', '4', '+'])
    assert result == 6, f'Wrong answer: {result}'
    result = calculate(['12', '5', '/', '4', '+'])
    assert result == 6, f'Wrong answer: {result}'
    result = calculate(['12', '5', '4', '+', '*'])
    assert result == 108, f'Wrong answer: {result}'
    result = calculate(
        ['12', '4', '/', '10', '*', '5', '6', '13', '-', '+', '/']
    )
    assert result == -15, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_calculate()
    print(calculate(input().split()))
