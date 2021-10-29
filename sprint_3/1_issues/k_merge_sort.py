def merge(array, _left, mid, right):
    left_index = right_index = 0
    left = array[_left:mid]
    right = array[mid:right]
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            array[_left+left_index+right_index] = left[left_index]
            left_index += 1
        else:
            array[_left+left_index+right_index] = right[right_index]
            right_index += 1
    while left_index < len(left):
        array[_left+left_index+right_index] = left[left_index]
        left_index += 1
    while right_index < len(right):
        array[_left+left_index+right_index] = right[right_index]
        right_index += 1
    return array


def merge_sort(array, left, right):
    if right - left <= 1:
        return
    mid = (left + right) // 2
    merge_sort(array, left, mid)
    merge_sort(array, mid, right)
    merge(array, left, mid, right)


# def _merge_sort(array):
#     if len(array) == 1:
#         return array
#     mid = len(array) // 2
#     left = merge_sort(array[:mid])
#     right = merge_sort(array[mid:])


# def test_merge_sort():
#     result = merge_sort([5, 1, 0, 2, 6, 5, 5, 4, 2, 3, 10])
#     assert result == [0, 1, 2, 2, 3, 4, 5, 5, 5, 6, 10], (
#         f'Wrong answer: {result}'
#     )
#     print('Все тесты пройдены!')


def test_merge_sort():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
    print('Все тесты пройдены!')


# if __name__ == '__main__':
#     test_merge_sort()
