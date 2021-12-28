def determine_max_sum(capacity, array):
    for index in range(len(array)):
        array[index] = [int(array[index][0]), int(array[index][1])]
    array.sort(key=lambda line: line[0], reverse=True)
    result = 0
    index = 0
    while capacity > 0 and index < len(array):
        difference = capacity - array[index][1]
        if difference >= 0:
            capacity = difference
            result += array[index][0] * array[index][1]
            index += 1
            continue
        capacity = 0
        result += array[index][0] * (array[index][1] + difference)
    return result


def test_determine_max_sum():
    result = determine_max_sum(10, [
        ['8', '1'],
        ['2', '10'],
        ['4', '5'],
    ])
    assert result == 36, f'Wrong answer: {result}'
    result = determine_max_sum(1000, [
        ['4', '20'],
    ])
    assert result == 80, f'Wrong answer: {result}'
    result = determine_max_sum(1, [
        ['4', '20'],
        ['1', '1'],
        ['33', '1'],
    ])
    assert result == 33, f'Wrong answer: {result}'
    result = determine_max_sum(0, [
        ['4', '20'],
        ['1', '1'],
        ['33', '1'],
    ])
    assert result == 0, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_determine_max_sum()
    capacity = int(input())
    count = int(input())
    array = [input().split() for _ in range(count)]
    print(determine_max_sum(capacity, array))
