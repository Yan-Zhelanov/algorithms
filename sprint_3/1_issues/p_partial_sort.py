def determine_max_count_of_blocks(array):
    result = 0
    index_min = array.index(min(array))
    while index_min < len(array):
        left = array[:index_min+1]
        right = array[index_min+1:]
        while left and right and max(left) >= min(right):
            index_min = array.index(min(array[index_min+1:]))
            left = array[:index_min+1]
            right = array[index_min+1:]
        index_min += 1
        result += 1
    return result


def test_determine_max_count_of_blocks():
    result = determine_max_count_of_blocks([3, 2, 0, 1, 4, 6, 5])
    assert result == 3, f'Wrong answer: {result}'
    result = determine_max_count_of_blocks([0, 1, 2, 3, 4])
    assert result == 5, f'Wrong answer: {result}'
    result = determine_max_count_of_blocks([1, 2, 3, 0])
    assert result == 1, f'Wrong answer: {result}'
    result = determine_max_count_of_blocks([1, 2, 3, 0])
    assert result == 1, f'Wrong answer: {result}'
    result = determine_max_count_of_blocks([1, 0, 3, 2])
    assert result == 2, f'Wrong answer: {result}'
    result = determine_max_count_of_blocks([1, 2, 3, 4, 0, 6, 7, 8, 5, 9])
    assert result == 3, f'Wrong answer: {result}'
    result = determine_max_count_of_blocks([0, 4, 1, 2, 3])
    assert result == 2, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_determine_max_count_of_blocks()
    input()
    print(determine_max_count_of_blocks(list(map(int, input().split()))))
