BUTTONS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def generate_texts(numbers, count=None, text='', result=''):
    if count is None:
        count = len(numbers)
    if count == 0:
        result += text + ' '
    else:
        for letter in BUTTONS[numbers[-count]]:
            result = generate_texts(numbers, count-1, text+letter, result)
    return result


def test_generate_texts():
    result = generate_texts('23')
    assert result == 'ad ae af bd be bf cd ce cf ', f'Wrong answer: {result}'
    result = generate_texts('689372357')
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_generate_texts()
    # print(generate_texts(input()))
