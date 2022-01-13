def is_same_sums(array):
    array.sort()
    index = 0
    while index < len(array):
        index += 1
        if sum(array[:index]) == sum(array[index:]):
            return True
    return False


def test_is_same_sums():
    result = is_same_sums([1, 7, 5, 1])
    assert result
    result = is_same_sums([1, 1, 1])
    assert not result
    result = is_same_sums([3, 5, 10])
    assert not result
    result = is_same_sums([7, 7, 1, 1, 2])
    assert result
    result = is_same_sums([])
    assert not result
    print('All tests passed!')


if __name__ == '__main__':
    test_is_same_sums()
