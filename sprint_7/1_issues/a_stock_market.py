def determine_max_income(array):
    max_income = 0
    day = 0
    buy = False
    while day < len(array):
        if buy:
            if day == len(array) - 1 or array[day] > array[day+1]:
                max_income += array[day]
                buy = False
        elif day+1 < len(array) and array[day] < array[day+1]:
            max_income -= array[day]
            buy = True
        day += 1
    return max_income


def test_determine_max_income():
    result = determine_max_income([7, 1, 5, 3, 6, 4])
    assert result == 7, f'Wrong answer: {result}'
    result = determine_max_income([1, 2, 3, 4, 5])
    assert result == 4, f'Wrong answer: {result}'
    result = determine_max_income([1, 12, 12, 16, 1, 8])
    assert result == 22, f'Wrong answer: {result}'
    result = determine_max_income([1, 1, 1, 1, 1])
    assert result == 0, f'Wrong answer: {result}'
    result = determine_max_income([])
    assert result == 0, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_determine_max_income()
    input()
    print(determine_max_income(list(map(int, input().split()))))
