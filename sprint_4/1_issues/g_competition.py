def determine_max_rounds_draw(rounds):
    def _hash(num):
        if num == '0':
            return -1
        return 1

    rounds = rounds.split()
    scores = []
    scores.append(_hash(rounds[0]))
    for index in range(len(rounds)-1):
        scores.append(scores[index] + _hash(rounds[index+1]))
    result = []
    for index in range(len(scores)):
        left = scores[index]
        rights = []
        try:
            rights.append(len(scores) - scores[left+1::-1].index(left+1) - 1)
        except ValueError:
            rights.append(index)
        try:
            rights.append(len(scores) - scores[left+1::-1].index(left-1) - 1)
        except ValueError:
            rights.append(index)
        right = max(rights)
        result.append(len(scores[index:right+1]))
    return max(result)


def test_determine_max_rounds_draw():
    result = determine_max_rounds_draw('0 1')
    assert result == 2, f'Wrong answer: {result}'
    result = determine_max_rounds_draw('0 1 0')
    assert result == 2, f'Wrong answer: {result}'
    result = determine_max_rounds_draw('0 0 1 0 1 1 1 0 0 0')
    assert result == 8, f'Wrong answer: {result}'
    result = determine_max_rounds_draw('1 1 1 1 1 0 0 0 0 0 1')
    assert result == 10, f'Wrong answer: {result}'
    result = determine_max_rounds_draw('0 1 0 1 0 0 0')
    assert result == 4, f'Wrong answer: {result}'
    result = determine_max_rounds_draw('0 0 0 0 0 1 0 1 0 0 0')
    assert result == 4, f'Wrong answer: {result}'
    result = determine_max_rounds_draw('1 1 1 1 1 0 1 0 1 0 1')
    assert result == 6, f'Wrong answer: {result}'
    result = determine_max_rounds_draw('1 1 1 1 0 1 0 1 1 1 1 1 0 1 0 1 0 1')
    assert result == 6, f'Wrong answer: {result}'
    result = determine_max_rounds_draw('0 0 1 0 0 0 1 0 0 1')
    assert result == 4, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_determine_max_rounds_draw()
    if input() == '0':
        print(0)
    else:
        print(determine_max_rounds_draw(input()))
