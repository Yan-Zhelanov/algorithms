def min_count_of_banknotes(need, banknotes):
    banknotes = sorted(
        [int(banknote) for banknote in banknotes],
        key=lambda banknote: -banknote,
    )
    index = 0
    result = 0
    while need != 0:
        result += need // banknotes[index]
        need %= banknotes[index]
        index += 1
    return result


def test_min_count_of_banknotes():
    result = min_count_of_banknotes(130, ['10', '3', '40', '1'])
    assert result == 4, f'Wrong answer: {result}'
    result = min_count_of_banknotes(100, ['7', '5'])
    assert result == 16, f'Wrong answer: {result}'
    result = min_count_of_banknotes(1, ['1'])
    assert result == 1, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_min_count_of_banknotes()
