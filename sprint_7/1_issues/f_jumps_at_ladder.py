def get_ways_to_step(end_step, max_step, module=1000000007):
    if end_step == 1:
        return 1
    dp = [0] * end_step
    dp[0] = dp[1] = 1
    for index in range(2, end_step):
        for step in range(1, max_step+1):
            if index-step < 0:
                break
            dp[index] += dp[index-step]
        dp[index] %= module
    return dp[-1]


def test_get_ways_to_step():
    result = get_ways_to_step(6, 3)
    assert result == 13, f'Wrong answer: {result}'
    result = get_ways_to_step(7, 7)
    assert result == 32, f'Wrong answer: {result}'
    result = get_ways_to_step(2, 2)
    assert result == 1, f'Wrong answer: {result}'
    result = get_ways_to_step(1, 10)
    assert result == 1, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_get_ways_to_step()
    end_step, max_step = input().split()
    print(get_ways_to_step(int(end_step), int(max_step)))
