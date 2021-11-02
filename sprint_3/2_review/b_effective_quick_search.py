from random import randint


def quick_sort(array):
    def _quick_sort(array, border_left, border_right):
        if border_left >= border_right:
            return array
        pivot = array[randint(border_left, border_right)]
        left, right = border_left, border_right
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quick_sort(array, border_left, right)
        _quick_sort(array, left, border_right)
        return array

    return _quick_sort(array, 0, len(array) - 1)


def preparation_data(array):
    index = 0
    while index < len(array):
        array[index] = [
            -int(array[index][1]), int(array[index][2]), array[index][0]
        ]
        index += 1
    return array


def get_winners_name(winners, index_name=2):
    return '\n'.join(winner[index_name] for winner in winners)


def test_quick_sort():
    result = quick_sort([10, 2, 3, 11, 5, 1])
    assert result == [1, 2, 3, 5, 10, 11], f'Wrong answer: {result}'
    result = quick_sort([0, 2, 3, 5, 5, 10, 13, -1])
    assert result == [-1, 0, 2, 3, 5, 5, 10, 13], f'Wrong answer: {result}'
    result = quick_sort([99, 10, -10, 30])
    assert result == [-10, 10, 30, 99], f'Wrong answer: {result}'
    result = quick_sort([33, 55, -1, -2, -3, 64])
    assert result == [-3, -2, -1, 33, 55, 64], f'Wrong answer: {result}'
    print(f'{__name__}: Все тесты пройдены!')


def test_get_winners():
    array = preparation_data([
        ['alla', '4', '100'],
        ['gena', '6', '1000'],
        ['gosha', '2', '90'],
        ['rita', '2', '90'],
        ['timofey', '4', '80'],
    ])
    array_sort = quick_sort(array)
    result = get_winners_name(array_sort)
    assert result == 'gena\ntimofey\nalla\ngosha\nrita', (
        f'Wrong answer: {result}'
    )
    print(f'{__name__}: Все тесты пройдены!')


if __name__ == '__main__':
    test_quick_sort()
    test_get_winners()
