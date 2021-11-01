def broken_search(nums, target):
    middle = len(nums) // 2
    left = 0
    right = len(nums)
    while left < right:
        if nums[middle] == target:
            return middle
        if left == middle or right == middle:
            break
        if (
            nums[middle] < target and min(nums[middle+1:]) <= target and max(nums[middle+1:]) >= target
            or nums[middle] > target and min(nums[:middle]) >= target and max(nums[:middle]) <= target
        ):
            left = middle
        else:
            right = middle
        middle = (left + right) // 2
    return -1


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
    assert result == 7, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_broken_search()