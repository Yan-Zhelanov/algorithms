def determine_max_collected_flowers(height, width, field):
    dp = [[0] * (width+1) for _ in range(height+1)]
    field = list(reversed(field))
    dp[1][1] = int(field[0][0])
    for line in range(1, height+1):
        for flower in range(1, width+1):
            dp[line][flower] = (
                max(dp[line-1][flower], dp[line][flower-1])
                + int(field[line-1][flower-1])
            )
    return dp[-1][-1]


def test_determine_max_collected_flowers():
    result = determine_max_collected_flowers(2, 3, [
        '101',
        '110',
    ])
    assert result == 3, f'Wrong answer: {result}'
    result = determine_max_collected_flowers(3, 3, [
        '100',
        '110',
        '001',
    ])
    result = determine_max_collected_flowers(3, 3, [
        '111',
        '111',
        '111',
    ])
    assert result == 5, f'Wrong answer: {result}'
    result = determine_max_collected_flowers(1, 1, ['1'])
    assert result == 1, f'Wrong answer: {result}'
    result = determine_max_collected_flowers(1, 1, ['0'])
    assert result == 0, f'Wrong answer: {result}'
    result = determine_max_collected_flowers(1, 3, ['000'])
    assert result == 0, f'Wrong answer: {result}'
    result = determine_max_collected_flowers(1, 3, ['111'])
    assert result == 3, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_determine_max_collected_flowers()
    height, width = input().split()
    height, width = int(height), int(width)
    field = [input() for _ in range(height)]
    print(determine_max_collected_flowers(height, width, field))
