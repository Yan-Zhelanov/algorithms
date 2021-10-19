# 54996852
def determine_nearest_zeros(array):
    zeros = []
    for index, num in enumerate(array):
        if num == '0':
            zeros.append(index)
    result = ''
    for index in range(0, zeros[0]):
        distance = zeros[0] - index
        result += f'{distance} '
    result += '0 '
    for left, right in zip(zeros[:-1], zeros[1:]):
        for index in range(left+1, right):
            distance = min(abs(index-left), abs(index-right))
            result += f'{distance} '
        result += '0 '
    for index in range(zeros[-1]+1, len(array)):
        distance = index - zeros[-1]
        result += f'{distance} '
    return result


def test_determine_nearest_zeros():
    result = determine_nearest_zeros(['0', '1', '4', '9', '0'])
    assert result == '0 1 2 1 0 ', f'Wrong answer: {result}'
    result = determine_nearest_zeros(['0', '7', '9', '4', '8', '20'])
    assert result == '0 1 2 3 4 5 ', f'Wrong answer: {result}'
    result = determine_nearest_zeros(['1', '7', '9', '4', '8', '20', '0'])
    assert result == '6 5 4 3 2 1 0 ', f'Wrong answer: {result}'
    result = determine_nearest_zeros(['1', '7', '9', '4', '8', '20', '0', '1'])
    assert result == '6 5 4 3 2 1 0 1 ', f'Wrong answer: {result}'
    result = determine_nearest_zeros(['0', '1', '0', '1', '0', '0', '99', '100'])
    assert result == '0 1 0 1 0 0 1 2 ', f'Wrong answer: {result}'
    result = determine_nearest_zeros(['2', '10', '20', '30', '0', '0', '99', '100'])
    assert result == '4 3 2 1 0 0 1 2 ', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_nearest_zeros()
    input()
    print(determine_nearest_zeros(input().split()))
