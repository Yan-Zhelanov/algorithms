def determine_sequences(size, count, text):
    sequences = {}
    index = 0
    result = set()
    while index < len(text):
        sequence = text[index:index+size]
        sequences[sequence] = sequences.get(sequence, 0) + 1
        index += 1
        sequence_index = text.index(sequence)
        if sequence_index in result:
            continue
        if sequences[sequence] >= count:
            result.add(sequence_index)
    return ' '.join(str(num) for num in result)


def test_determine_sequences():
    result = determine_sequences(10, 2, 'gggggooooogggggoooooogggggssshaa')
    assert result == '0 5', f'Wrong answer: {result}'
    result = determine_sequences(3, 4, 'allallallallalla')
    assert result == '0 1 2', f'Wrong answer: {result}'
    result = determine_sequences(4, 2, 'golllllllal')
    assert result == '2', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_determine_sequences()
    size, count = input().split()
    size, count = int(size), int(count)
    print(determine_sequences(size, count, input()))
