BUTTONS = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
}


def generate_texts(numbers):
    result = []
    count = len(numbers)
    while count > 0:
        text = ''
        for letter in BUTTONS[int(numbers[-count])]:
            text += letter
            result.append(text)
        count -= 1
    return ' '.join(result)


def test_generate_texts():
    result = generate_texts('23')
    assert result == 'ad ae af bd be bf cd ce cf', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_generate_texts()
    print(generate_texts(input()))
