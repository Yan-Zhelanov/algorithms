# 54997842
def get_score(array, count, players=2, skip='.'):
    array = ''.join(array)
    count *= players
    buttons = {}
    for button in array:
        if button == skip:
            continue
        if buttons.get(button):
            buttons[button] += 1
            continue
        buttons[button] = 1
    return sum(1 for value in buttons.values() if value <= count)


def test_get_score():
    array = ['1223', '2..2', '2..2', '2..2']
    result = get_score(array, 3)
    assert result == 2, f'Wrong answer: {result}'
    array = ['1111', '9999', '1111', '9911']
    result = get_score(array, 4)
    assert result == 1, f'Wrong answer: {result}'
    array = ['1111', '1111', '1111', '1111']
    result = get_score(array, 4)
    assert result == 0, f'Wrong answer: {result}'
    array = ['....', '....', '....', '....']
    result = get_score(array, 100)
    assert result == 0, f'Wrong answer: {result}'
    array = ['1111', '2222', '3343', '4444']
    result = get_score(array, 2)
    assert result == 3, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_get_score()
    count = int(input())
    array = [input() for _ in range(4)]
    print(get_score(array, count))
