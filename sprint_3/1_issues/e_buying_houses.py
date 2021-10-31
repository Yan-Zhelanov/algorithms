def determine_max_houses_to_buy(money, coasts):
    coasts.sort()
    result = 0
    for coast in coasts:
        if money >= coast:
            result += 1
            money -= coast
            continue
        break
    return result


def test_determine_max_houses_to_buy():
    result = determine_max_houses_to_buy(300, [999, 300, 999])
    assert result == 1, f'Wrong answer: {result}'
    result = determine_max_houses_to_buy(1, [999, 300, 999])
    assert result == 0, f'Wrong answer: {result}'
    result = determine_max_houses_to_buy(999, [999, 300, 999])
    assert result == 1, f'Wrong answer: {result}'
    result = determine_max_houses_to_buy(6, [3, 2, 1])
    assert result == 3, f'Wrong answer: {result}'
    result = determine_max_houses_to_buy(5, [3, 1, 2])
    assert result == 2, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_max_houses_to_buy()
    _, money = input().split()
    money = int(money)
    print(determine_max_houses_to_buy(money, list(map(int, input().split()))))
