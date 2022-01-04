def determine_route_with_max_flowers(height, width, field):
    field = list(reversed(field))
    dp = [[0] * (width+1) for _ in range(height+1)]
    dp[1][1] = int(field[0][0])
    route = []
    for line in range(1, height+1):
        for flower in range(1, width+1):
            dp[line][flower] = (
                max(dp[line-1][flower], dp[line][flower-1])
                + int(field[line-1][flower-1])
            )
    count = width + height - 2
    line, flower = height, width
    while len(route) != count:
        if line - 1 == 0:
            route.append('R')
            continue
        elif flower - 1 == 0:
            route.append('U')
            continue
        if dp[line-1][flower] >= dp[line][flower-1]:
            route.append('U')
            line -= 1
            continue
        flower -= 1
        route.append('R')
    return f'{dp[-1][-1]}' if len(route) == 0 else (
        f'{dp[-1][-1]}\n' + ''.join(list(reversed(route)))
    )


def test_determine_route_with_max_flowers():
    result = determine_route_with_max_flowers(5, 5, [
        '00101',
        '00110',
        '11010',
        '11001',
        '01010',
    ])
    assert result == '6\nRUURRURU', f'Wrong answer: {result}'
    result = determine_route_with_max_flowers(2, 3, [
        '101',
        '110',
    ])
    assert result == '3\nRRU', f'Wrong answer: {result}'
    result = determine_route_with_max_flowers(3, 3, [
        '100',
        '110',
        '001',
    ])
    assert result == '2\nURRU', f'Wrong answer: {result}'
    result = determine_route_with_max_flowers(1, 1, ['0'])
    assert result == '0', f'Wrong answer: {result}'
    result = determine_route_with_max_flowers(1, 1, ['1'])
    assert result == '1', f'Wrong answer: {result}'
    result = determine_route_with_max_flowers(1, 3, ['111'])
    assert result == '3\nRR', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_determine_route_with_max_flowers()
    height, width = input().split()
    width, height = int(width), int(height)
    field = [input() for _ in range(height)]
    print(determine_route_with_max_flowers(height, width, field))
