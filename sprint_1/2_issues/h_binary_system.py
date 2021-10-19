def binary_sum(num_1, num_2):
    if int(num_1) != max(int(num_1), int(num_2)):
        num_1, num_2 = num_2, num_1
    result = ''
    remains = 0
    i = 1
    left = len(num_1)
    while i <= left:
        try:
            temp = int(num_1[-i]) + int(num_2[-i]) + remains
        except IndexError:
            temp = int(num_1[-i]) + remains
        if temp == 0:
            remains = 0
            result += '0'
        elif temp == 1:
            remains = 0
            result += '1'
        elif temp == 2:
            remains = 1
            result += '0'
        else:
            remains = 1
            result += '1'
        i += 1
    result += str(remains)
    return int(''.join(result[i] for i in range(len(result)-1, -1, -1)))


def test_binary_sum():
    result = binary_sum('1010', '1011')
    assert result == 10101, f'Wrong answer: {result}'
    result = binary_sum('1', '1')
    assert result == 10, f'Wrong answer: {result}'
    result = binary_sum('101', '1011')
    assert result == 10000, f'Wrong answer: {result}'
    result = binary_sum('0', '0')
    assert result == 0, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    print(binary_sum(input(), input()))
