SEQUENCE_1 = 0
SEQUENCE_2 = 1


def determine_max_subsequence_length_and_indexes(sequence_1, sequence_2):
    dp = [[0] * (len(sequence_1)+1) for _ in range(len(sequence_2)+1)]
    for index_char_1 in range(1, len(sequence_2)+1):
        for index_char_2 in range(1, len(sequence_1)+1):
            if sequence_1[index_char_2-1] != sequence_2[index_char_1-1]:
                dp[index_char_1][index_char_2] = max(
                    dp[index_char_1-1][index_char_2],
                    dp[index_char_1][index_char_2-1],
                )
                continue
            dp[index_char_1][index_char_2] = (
                dp[index_char_1-1][index_char_2-1] + 1
            )
    if dp[-1][-1] == 0:
        return '0'
    answer = [[], []]
    width, height = len(sequence_1), len(sequence_2)
    while dp[height][width] != 0:
        if sequence_1[width-1] == sequence_2[height-1]:
            answer[SEQUENCE_1].append(width)
            answer[SEQUENCE_2].append(height)
            width -= 1
            height -= 1
        elif dp[height][width] == dp[height-1][width]:
            height -= 1
        elif dp[height][width] == dp[height][width-1]:
            width -= 1
    answer = [
        list(reversed(answer[SEQUENCE_1])),
        list(reversed(answer[SEQUENCE_2])),
    ]
    return f'{dp[-1][-1]}\n' + '\n'.join(
        ' '.join(str(index) for index in line)
        for line in answer
    )


def test_determine_max_subsequence_length_and_indexes():
    result = determine_max_subsequence_length_and_indexes(
        ['4', '9', '2', '4', '6'],
        ['9', '4', '0', '0', '2', '8', '4'],
    )
    assert result == '3\n2 3 4\n1 5 7', f'Wrong answer: {result}'
    result = determine_max_subsequence_length_and_indexes(
        ['1', '1', '1', '1'],
        ['2', '2'],
    )
    assert result == '0', f'Wrong answer: {result}'
    result = determine_max_subsequence_length_and_indexes(
        ['1', '2', '1', '9', '1', '2', '1', '9'],
        ['9', '9', '1', '9', '9'],
    )
    assert result == '3\n4 7 8\n1 3 5', f'Wrong answer: {result}'
    result = determine_max_subsequence_length_and_indexes(
        ['1'],
        ['1'],
    )
    assert result == '1\n1\n1', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_determine_max_subsequence_length_and_indexes()
    input()
    sequence_1 = input().split()
    input()
    sequence_2 = input().split()
    print(determine_max_subsequence_length_and_indexes(sequence_1, sequence_2))
