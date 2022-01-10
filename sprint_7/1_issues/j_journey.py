def determine_max_increasing_sequence_size_and_indexes(sequence):
    dp = [0] * (len(sequence)+1)
    for index in range(2, len(sequence)+1):
        if index < len(sequence) and sequence[index-2] < sequence[index-1]:
            dp[index] = dp[index-1] + 1
            continue
        max_len = 0
        for index_2 in range(index-3, 0, -1):
            if sequence[index_2] < sequence[index-1]:
                max_len = max(max_len, dp[index_2])
        dp[index] = max_len
    return dp[-1]


def test_determine_max_increasing_sequence_size_and_indexes():
    result = determine_max_increasing_sequence_size_and_indexes([
        '4', '2', '9', '1', '13',
    ])
    assert result == '3\n1 3 5', f'Wrong answer: {result}'
    result = determine_max_increasing_sequence_size_and_indexes([
        '1', '2', '4', '8', '16', '32',
    ])
    assert result == '6\n1 2 3 4 5 6', f'Wrong answer: {result}'
    result = determine_max_increasing_sequence_size_and_indexes(['1'])
    assert result == '1\n1', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_determine_max_increasing_sequence_size_and_indexes()
