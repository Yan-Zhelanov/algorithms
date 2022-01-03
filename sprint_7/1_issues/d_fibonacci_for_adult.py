def get_fibonacci(n, module=1000000007):
    if n == 0:
        return 1
    dp = [None] * (n+1)
    dp[0] = dp[1] = 1
    for index in range(2, n+1):
        dp[index] = (dp[index-1] + dp[index-2]) % module
    return dp[n]


def test_get_fibonacci():
    result = get_fibonacci(0)
    assert result == 1, f'Wrong answer: {result}'
    result = get_fibonacci(1)
    assert result == 1, f'Wrong answer: {result}'
    result = get_fibonacci(5)
    assert result == 8, f'Wrong answer: {result}'
    result = get_fibonacci(2)
    assert result == 2, f'Wrong answer: {result}'
    result = get_fibonacci(10)
    assert result == 89, f'Wrong answer: {result}'
    result = get_fibonacci(66)
    assert result == 569898238, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_get_fibonacci()
    print(get_fibonacci(int(input())))
