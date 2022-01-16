def is_same_sums(array):
    if len(array) == 0:
        return False
    array.sort(reverse=True)
    left = array[0]
    right = 0
    index = 1
    while index < len(array):
        if left < right:
            left += array[index]
        else:
            right += array[index]
        index += 1
    return left == right


def test_is_same_sums():
    result = is_same_sums([1, 7, 5, 1])
    assert result
    result = is_same_sums([1, 1, 1])
    assert not result
    result = is_same_sums([3, 5, 10])
    assert not result
    result = is_same_sums([7, 7, 1, 1, 2])
    assert result
    result = is_same_sums([1, 2, 3, 4, 5, 1])
    assert result
    result = is_same_sums([2, 2, 3, 4, 5, 10])
    assert not result
    result = is_same_sums([])
    assert not result
    print('All tests passed!')


if __name__ == '__main__':
    # test_is_same_sums()
    input()
    print(is_same_sums(list(map(int, input().split()))))
