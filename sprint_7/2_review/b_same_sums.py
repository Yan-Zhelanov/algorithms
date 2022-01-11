def is_same_sums(array):
    pass


def test_is_same_sums():
    result = is_same_sums([1, 7, 5, 1])
    assert result
    result = is_same_sums([1, 1, 1])
    assert not result
    result = is_same_sums([3, 5, 10])
    assert not result
    result = is_same_sums([])
    assert result
    print('All tests passed!')


if __name__ == '__main__':
    test_is_same_sums()
