def determine_max_rounds_draw(rounds):
    def _hash(num):
        if num == '0':
            return -1
        return 1

    score = 0
    scores = {0: [0]}
    max_score = 0
    for index, lap in enumerate(rounds.split()):
        score += _hash(lap)
        scores[score] = scores.get(score, []) + [index]
        if len(scores[score]) > 2:
            scores[score] = [scores[score][0], scores[score][-1]]
        if len(scores[score]) == 2:
            size = scores[score][-1] - scores[score][0]
            if max_score < size:
                max_score = size
    return max_score


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
    result = determine_max_rounds_draw('0 0 1 1 1 0 0 1 1')
    assert result == 8, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_determine_max_rounds_draw()
    if input() == '0':
        print(0)
    else:
        print(determine_max_rounds_draw(input()))
