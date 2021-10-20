# 55081941
def determine_nearest_zeros(array):
    distance = float('inf')
    result = [0] * len(array)
    for index, num in enumerate(array):
        if num == '0':
            distance = 1
            continue
        result[index] = distance
        distance += 1
    distance = float('inf')
    for index, num in enumerate(reversed(array)):
        if num == '0':
            distance = 1
            continue
        result[-(index+1)] = min(result[-(index+1)], distance)
        distance += 1
    return ' '.join(str(num) for num in result)


def test_determine_nearest_zeros():
    result = determine_nearest_zeros(['0', '1', '4', '9', '0'])
    assert result == '0 1 2 1 0', f'Wrong answer: {result}'
    result = determine_nearest_zeros(['0', '7', '9', '4', '8', '20'])
    assert result == '0 1 2 3 4 5', f'Wrong answer: {result}'
    result = determine_nearest_zeros(['1', '7', '9', '4', '8', '20', '0'])
    assert result == '6 5 4 3 2 1 0', f'Wrong answer: {result}'
    result = determine_nearest_zeros(['1', '7', '9', '4', '8', '20', '0', '1'])
    assert result == '6 5 4 3 2 1 0 1', f'Wrong answer: {result}'
    result = determine_nearest_zeros(['0', '1', '0', '1', '0', '0', '99', '100'])
    assert result == '0 1 0 1 0 0 1 2', f'Wrong answer: {result}'
    result = determine_nearest_zeros(['2', '10', '20', '30', '0', '0', '99', '100'])
    assert result == '4 3 2 1 0 0 1 2', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_nearest_zeros()
    input()
    print(determine_nearest_zeros(input().split()))
