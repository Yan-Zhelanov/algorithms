def counting_sort(array, count=3):
    counts = [0] * count
    for num in array:
        counts[int(num)] += 1
    result = ''
    for index, count in enumerate(counts):
        for _ in range(count):
            result += f'{index} '
    return result


def test_counting_sort():
    array = ['0', '1', '2', '0', '1', '2', '0']
    result = counting_sort(array)
    assert result == '0 0 0 1 1 2 2', f'Wrong answer: {result}'
    array = ['0', '0', '0', '0', '0']
    result = counting_sort(array)
    assert result == '0 0 0 0 0', f'Wrong answer: {result}'
    array = ['0', '1', '0', '0', '0']
    result = counting_sort(array)
    assert result == '0 0 0 0 1', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_counting_sort()
    input()
    print(counting_sort(input().split()))
