def determine_chaotic(array):
    if len(array) == 1:
        return 1
    result = 0
    for index in range(len(array)):
        temp = 0
        r = array[index-1]
        if index - 1 >= 0:
            if array[index-1] < array[index]:
                temp += 1
        else:
            temp += 1
        try:
            if array[index] > array[index+1]:
                temp += 1
        except IndexError:
            temp += 1
        if temp == 2:
            result += 1
    return result
            


def test_determine_chaotic():
    result = determine_chaotic([-1, -10, -8, 0, 2, 0, 5])
    assert result == 3, f'Wrong answer: {result}'
    result = determine_chaotic([1, 2, 5, 4, 8])
    assert result == 2, f'Wrong answer: {result}'
    result = determine_chaotic([1])
    assert result == 1, f'Wrong answer: {result}'
    result = determine_chaotic([0, 1])
    assert result == 1, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    input()
    print(determine_chaotic(list(map(int, input().split()))))
