from random import randint


def quick_sort(array):
    def _quick_sort(array, border_left, border_right):
        if border_left >= border_right:
            return array
        pivot = randint(border_left, border_right)
        left = border_left
        right = border_right
        while left < right:
            while left < border_right and array[left] < array[pivot]:
                left += 1
            while right > border_left and array[right] > array[pivot]:
                right -= 1
            array[left], array[right] = array[right], array[left]
        _quick_sort(array, left, border_right)
        _quick_sort(array, border_left, right)
        return array

    return _quick_sort(array, 0, len(array) - 1)


def preparation_data(array):
    index = 0
    while index < len(array):
        array[index] = [
            -int(array[index][1]), int(array[index][2]), array[index][0]
        ]
    return array


def test_quick_sort():
    array = [10, 2, 3, 11, 5, 1]
    result = quick_sort(array)
    assert result == [1, 2, 3, 5, 10, 11], f'Wrong answer: {result}'
    array = preparation_data([
        ['alla', '4', '100'],
        ['gena', '6', '1000'],
        ['gosha', '2', '90'],
        ['rita', '2', '90'],
        ['timofey', '4', '80'],
    ])
    result = quick_sort(array)
    assert result == 'gena\ntimofey\nalla\ngosha\nrita', (
        f'Wrong answer: {result}'
    )
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_quick_sort()
