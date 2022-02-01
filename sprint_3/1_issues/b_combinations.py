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


def generate_texts(numbers):
    def _generate_sequences(numbers, count=None, text='', result=[]):
        if count is None:
            count = len(numbers)
        if count == 0:
            result.append(text)
            return result
        for letter in BUTTONS[numbers[-count]]:
            result = _generate_sequences(numbers, count-1, text+letter, result)
        return result

    return ' '.join(_generate_sequences(numbers))


def test_generate_texts():
    result = generate_texts('23')
    assert result == 'ad ae af bd be bf cd ce cf', f'Wrong answer: {result}'
    result = generate_texts('2')
    assert result == 'a b c', f'Wrong answer: {result}'
    result = generate_texts('22')
    assert result == 'aa ab ac ba bb bc ca cb cc', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_generate_texts()
    print(generate_texts(input()))
