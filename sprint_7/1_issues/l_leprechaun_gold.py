def determine_max_gold(count_bars, max_weight, bars):
    if count_bars == 0:
        return 0
    max_weight += 1
    dp = [0] * max_weight
    for bar in range(count_bars):
        current = [0] * max_weight
        bars[bar] = int(bars[bar])
        for weight in range(1, max_weight):
            if bars[bar] > weight:
                current[weight] = dp[weight]
            elif bar == 0:
                current[weight] = bars[bar]
            elif weight - bars[bar] <= 0:
                current[weight] = max(bars[bar], dp[weight])
            else:
                current[weight] = max(
                    dp[weight],
                    dp[weight-bars[bar]] + bars[bar],
                )
        dp = current
    return dp[-1]


def test_determine_max_gold():
    result = determine_max_gold(5, 15, ['3', '8', '1', '2', '5'])
    assert result == 15, f'Wrong answer: {result}'
    result = determine_max_gold(5, 19, ['10', '10', '7', '7', '4'])
    assert result == 18, f'Wrong answer: {result}'
    result = determine_max_gold(5, 5, ['1', '1', '3', '6', '4'])
    assert result == 5, f'Wrong answer: {result}'
    result = determine_max_gold(3, 10, ['1', '1', '1'])
    assert result == 3, f'Wrong answer: {result}'
    result = determine_max_gold(0, 100, [])
    assert result == 0, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_determine_max_gold()
    count_bars, weight = input().split()
    bars = input().split()
    print(determine_max_gold(int(count_bars), int(weight), bars))
