WEIGHT = 0
WORST = 1


def determine_max_things_and_indexes(max_weight, things):
    if len(things) == 0 or max_weight == 0:
        return '0'
    max_weight += 1
    dp = [[0] * max_weight for _ in range(len(things))]
    for thing in range(len(things)):
        things[thing] = [int(things[thing][WEIGHT]), int(things[thing][WORST])]
        for weight in range(1, max_weight):
            if things[thing][WEIGHT] > weight:
                dp[thing][weight] = dp[thing-1][weight]
            elif thing == 0:
                dp[thing][weight] = things[thing][1]
            elif weight - things[thing][WEIGHT] <= 0:
                dp[thing][weight] = max(
                    things[thing][WORST],
                    dp[thing-1][weight],
                )
            else:
                dp[thing][weight] = max(
                    dp[thing-1][weight],
                    (
                        dp[thing-1][weight-things[thing][WEIGHT]]
                        + things[thing][WORST]
                    ),
                )
    return dp[-1][-1]


def test_determine_max_things_and_indexes():
    result = determine_max_things_and_indexes(6, [
        ['2', '7'],
        ['4', '2'],
        ['1', '5'],
        ['2', '1'],
    ])
    assert result == '3\n4 3 1', f'Wrong answer: {result}'
    result = determine_max_things_and_indexes(0, [['2', '7']])
    assert result == '0', f'Wrong answer: {result}'
    result = determine_max_things_and_indexes(10, [])
    assert result == '0', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_determine_max_things_and_indexes()
