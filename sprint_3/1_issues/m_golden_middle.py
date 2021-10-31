def determine_median(array_1, array_2):
    array = sorted(array_1 + array_2)
    middle = len(array) // 2
    if len(array) % 2 == 0:
        middle_sum = array[middle-1] + array[middle]
        return middle_sum // 2 if middle_sum % 2 == 0 else middle_sum / 2
    return array[middle]


def test_determine_median():
    result = determine_median([1, 3], [2])
    assert result == 2, f'Wrong answer: {result}'
    result = determine_median([1, 3, 4], [2])
    assert result == 2.5, f'Wrong answer: {result}'
    result = determine_median([1, 3, 4], [2, 5])
    assert result == 3, f'Wrong answer: {result}'
    result = determine_median([1, 3, 4], [2, 5, 6])
    assert result == 3.5, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_median()
    input()
    input()
    print(determine_median(
        list(map(int, input().split())), list(map(int, input().split()))
    ))
