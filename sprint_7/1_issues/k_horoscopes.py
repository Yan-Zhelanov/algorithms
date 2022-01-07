def determine_max_subsequence_length_and_indexes(sequence_1, sequence_2):
    pass


def test_determine_max_subsequence_length_and_indexes():
    result = determine_max_subsequence_length_and_indexes(
        ['4', '9', '2', '4', '6'],
        ['9', '4', '0', '0', '2', '8', '4'],
    )
    assert result == '3\n1 3 4\n2 5 7', f'Wrong answer: {result}'
    result = determine_max_subsequence_length_and_indexes(
        ['1', '1', '1', '1'],
        ['2', '2'],
    )
    assert result == '0', f'Wrong answer: {result}'
    result = determine_max_subsequence_length_and_indexes(
        ['1', '2', '1', '9', '1', '2', '1', '9'],
        ['9', '9', '1', '9', '9'],
    )
    assert result == '3\n3 4 8\n3 4 5', f'Wrong answer: {result}'
    result = determine_max_subsequence_length_and_indexes(
        ['1'],
        ['1'],
    )
    assert result == '1\n1\n1', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_determine_max_subsequence_length_and_indexes()
