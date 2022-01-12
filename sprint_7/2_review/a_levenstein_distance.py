def determine_levenstein_distance(string_1, string_2):
    dp = [[0] * (len(string_2)+1) for _ in range(len(string_1)+1)]
    for i in range(1, len(string_1)+1):
        for j in range(1, len(string_2)+1):
            if string_1[i-1] == string_2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                continue
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return max(len(string_1), len(string_2)) - dp[-1][-1]


def test_determine_levenstein_distance():
    result = determine_levenstein_distance('queue', 'ueue')
    assert result == 1, f'Wrong answer: {result}'
    result = determine_levenstein_distance('abacaba', 'abaabc')
    assert result == 2, f'Wrong answer: {result}'
    result = determine_levenstein_distance('innokentiy', 'innnokkentia')
    assert result == 3, f'Wrong answer: {result}'
    result = determine_levenstein_distance('qeeq', 'uuiq')
    assert result == 3, f'Wrong answer: {result}'
    result = determine_levenstein_distance('qeep', 'uuiq')
    assert result == 4, f'Wrong answer: {result}'
    result = determine_levenstein_distance('r', 'x')
    assert result == 1, f'Wrong answer: {result}'
    result = determine_levenstein_distance('q', 'q')
    assert result == 0, f'Wrong answer: {result}'
    result = determine_levenstein_distance('', 'x')
    assert result == 1, f'Wrong answer: {result}'
    result = determine_levenstein_distance('', '')
    assert result == 0, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_determine_levenstein_distance()
    print(determine_levenstein_distance(input(), input()))
