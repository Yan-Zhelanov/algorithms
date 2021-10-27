def generate_brackets(count, open=0, sequence='', sequences=None):
    if sequences is None:
        sequences = []
    if count == 0:
        sequences.append(sequence)
    elif count > open:
        generate_brackets(count-1, open+1, sequence+'(', sequences)
    if open > 0:
        generate_brackets(count-1, open-1, sequence+')', sequences)
    return '\n'.join(sequences)


def test_generate_brackets():
    result = generate_brackets(4)
    assert result == '(())\n()()', f'Wrong answer: {result}'
    result = generate_brackets(6)
    assert result == '((()))\n(()())\n(())()\n()(())\n()()()', (
        f'Wrong answer: {result}'
    )
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_generate_brackets()
    print(generate_brackets(int(input())*2))
