def is_difference_one_unit(string_1, string_2):
    if len(string_1) > len(string_2):
        string_1, string_2 = string_2, string_1
    dp = [[0] * (len(string_1)+1) for _ in range(2)]
    for i in range(len(string_2)+1):
        for j in range(len(string_1)+1):
            if i == 0:
                dp[1][j] = j
                continue
            if j == 0:
                dp[1][j] = i
                continue
            action = 0
            if string_1[j-1] != string_2[i-1]:
                action = 1
            dp[1][j] = min(dp[0][j]+1, dp[1][j-1]+1, dp[0][j-1]+action)
        dp[0] = list(dp[1])
    return 'OK' if dp[-1][-1] <= 1 else 'FAIL'


def test_is_difference_one_unit():
    result = is_difference_one_unit('Коля', 'оля')
    assert result == 'OK'
    result = is_difference_one_unit('Коляя', 'оля')
    assert result == 'FAIL'
    result = is_difference_one_unit('hello', 'helo')
    assert result == 'OK'
    result = is_difference_one_unit('dog', 'fog')
    assert result == 'OK'
    result = is_difference_one_unit('mama', 'papa')
    assert result == 'FAIL'
    print('All tests passed!')


if __name__ == '__main__':
    # test_is_difference_one_unit()
    print(is_difference_one_unit(input(), input()))
