# 56006146
def broken_search(array, target):
    def _binary_search(array, target, left, right):
        while left <= right:
            middle = (left + right) // 2
            if array[middle] == target:
                return middle
            if array[left] == target:
                return left
            if array[right] == target:
                return right
            if target < array[middle]:
                right = middle - 1
            elif target > array[middle]:
                left = middle + 1
        return -1

    def _find_break(array):
        left = 0
        right = len(array) - 1
        while left <= right:
            middle = (left + right) // 2
            if left < middle and array[middle-1] > array[middle]:
                return middle - 1
            elif middle < right and array[middle] > array[middle+1]:
                return middle
            if array[left] >= array[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return -1

    index_break = _find_break(array)
    if index_break == -1:
        return _binary_search(array, target, 0, len(array)-1)
    if array[index_break] == target:
        return index_break
    if array[0] <= target < array[index_break]:
        return _binary_search(array, target, 0, index_break-1)
    return _binary_search(array, target, index_break+1, len(array)-1)


def test_broken_search():
    result = broken_search([19, 21, 100, 101, 1, 4, 5, 7, 12], 5)
    assert result == 6, f'Wrong answer: {result}'
    result = broken_search([1, 2, 3, 4, 5, 6, 7, 8, 0], 7)
    assert result == 6, f'Wrong answer: {result}'
    result = broken_search([-33, 0, 15, 16, 18, 44, -55, -35], 44)
    assert result == 5, f'Wrong answer: {result}'
    result = broken_search([100, 0, 1, 2, 3, 44, 55, 73, 99], 0)
    assert result == 1, f'Wrong answer: {result}'
    result = broken_search([100, 0, 1, 2, 3, 44, 55, 73, 99], 99)
    assert result == 8, f'Wrong answer: {result}'
    result = broken_search([100, 0, 1, 2, 3, 44, 55, 73, 99], 100)
    assert result == 0, f'Wrong answer: {result}'
    result = broken_search([100, 0, 1, 2, 3, 44, 55, 73, 99], -100)
    assert result == -1, f'Wrong answer: {result}'
    result = broken_search([0, 1, 2, 3, 44, 55, 73, 99, -33], 44)
    assert result == 4, f'Wrong answer: {result}'
    result = broken_search([0, 1, 2, 3, 44, 55, 73, 99, -33], 0)
    assert result == 0, f'Wrong answer: {result}'
    result = broken_search([0, 1, 2, 3, 44, 55, 73, 99, -33], -33)
    assert result == 8, f'Wrong answer: {result}'
    result = broken_search([0, 1, 2, 3, 44, 55, 73, 99, -33], -99)
    assert result == -1, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


# if __name__ == '__main__':
#     test_broken_search()
