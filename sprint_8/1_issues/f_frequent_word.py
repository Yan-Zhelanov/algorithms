def determine_frequent_word(words):
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return sorted(list(result.items()), key=lambda item: (-item[1], item[0]))[0][0]


def test_determine_frequent_word():
    result = determine_frequent_word([
        'sadasd',
        'dasdsadas',
        'ae',
        'sadasd',
        'sadasd',
        'ae',
    ])
    assert result == 'sadasd', f'Wrong answer: {result}'
    result = determine_frequent_word([
        'a',
        'be',
        'ce',
    ])
    assert result == 'a', f'Wrong answer: {result}'
    result = determine_frequent_word([
        'kek',
    ])
    assert result == 'kek', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_determine_frequent_word()
    print(determine_frequent_word([input() for _ in range(int(input()))]))
