def determine_max_rounds_draw(rounds):
    rounds = rounds.split()
    if rounds[0] == '0':
        scores = [[1, 0]]
    else:
        scores = [[0, 1]]
    for index in range(len(rounds)-1):
        score = [scores[index][0], scores[index][1]]
        score[int(rounds[index+1])] += 1
        scores.append(score)
    result = []
    for index in range(len(scores)):
        left = scores[index]
        try:
            if left <= 0:
                right = len(scores) - scores[::-1].index(left+1) - 1
            else:
                right = len(scores) - scores[::-1].index(left-1) - 1
        except ValueError:
            continue
        result.append(len(scores[index:right+1]))
    return max(result)


def test_determine_max_rounds_draw():
    result = determine_max_rounds_draw('0 1 1 1 0 1 0 1 1')
    assert result == 2, f'Wrong answer: {result}'
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
