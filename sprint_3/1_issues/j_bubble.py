def bubble_sort(array):
    result = ''
    size = len(array) - 1
    while size > 0:
        index = 0
        changed = False
        while index < size:
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                changed = True
            index += 1
        if changed:
            result += ' '.join(str(num) for num in array) + '\n'
        size -= 1
    return result if result != '' else ' '.join(str(num) for num in array)


def test_bubble_sort():
    result = bubble_sort([4, 3, 9, 2, 1])
    assert result == '3 4 2 1 9\n3 2 1 4 9\n2 1 3 4 9\n1 2 3 4 9\n', (
        f'Wrong answer: {result}'
    )
    result = bubble_sort([2, 1, 1, 1, 1])
    assert result == '1 1 1 1 2\n', (
        f'Wrong answer: {result}'
    )
    result = bubble_sort([1, 1, 1, 1, 1])
    assert result == '1 1 1 1 1', (
        f'Wrong answer: {result}'
    )
    result = bubble_sort([4, 6, 2, 7, 1])
    assert result == '4 2 6 1 7\n2 4 1 6 7\n2 1 4 6 7\n1 2 4 6 7\n', (
        f'Wrong answer: {result}'
    )
    result = bubble_sort([2, 3, 1])
    assert result == '2 1 3\n1 2 3\n', (
        f'Wrong answer: {result}'
    )
    result = bubble_sort([4, 5])
    assert result == '4 5', (
        f'Wrong answer: {result}'
    )
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_bubble_sort()
    input()
    print(bubble_sort(list(map(int, input().split()))))
