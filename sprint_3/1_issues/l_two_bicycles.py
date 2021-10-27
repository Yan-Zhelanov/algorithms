def binary_search(array, num, left=0, right=None):
    right = len(array) if right is None else right
    mid = (left + right) // 2
    if right <= left:
        return -1
    if array[mid] >= num:
        nearest = binary_search(array, num, left, mid)
        return mid if nearest == -1 else nearest
    else:
        return binary_search(array, num, mid+1, right)


def search_two_days(array, coast):
    first = binary_search(array, coast)
    if first != -1:
        first += 1
    second = binary_search(array, coast*2)
    if second != -1:
        second += 1
    return f'{first} {second}'


def test_search_two_days():
    result = search_two_days([1, 2, 4, 4, 6, 8], 3)
    assert result == '3 5', f'Wrong answer: {result}'
    result = search_two_days([1, 2, 10, 10, 10, 11], 10)
    assert result == '3 -1', f'Wrong answer: {result}'
    result = search_two_days([1, 2, 3, 4, 5, 6, 6], 10)
    assert result == '-1', f'Wrong answer: {result}'
    result = search_two_days([2, 4], 2)
    assert result == '1 2', f'Wrong answer: {result}'
    result = search_two_days([2, 4, 4, 4, 5, 5], 4)
    assert result == '2 -1', f'Wrong answer: {result}'
    result = search_two_days([1], 4)
    assert result == '-1', f'Wrong answer: {result}'
    result = search_two_days([4], 4)
    assert result == '1 -1', f'Wrong answer: {result}'
    result = search_two_days([4], 2)
    assert result == '1 1', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_search_two_days()
    input()
    print(search_two_days(list(map(int, input().split())), int(input())))
