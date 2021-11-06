# 56013109
import traceback
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


def determine_winners(participants, name=0, score=1, penalty=2):
    participants = list(map(lambda participant: [
        -int(participant[score]), int(participant[penalty]), participant[name],
    ], participants))
    quick_sort(participants)
    return '\n'.join(participant[2] for participant in participants)


def test_quick_sort():
    result = quick_sort([10, 2, 3, 11, 5, 1])
    assert result == [1, 2, 3, 5, 10, 11], f'Wrong answer: {result}'
    result = quick_sort([0, 2, 3, 5, 5, 10, 13, -1])
    assert result == [-1, 0, 2, 3, 5, 5, 10, 13], f'Wrong answer: {result}'
    result = quick_sort([99, 10, -10, 30])
    assert result == [-10, 10, 30, 99], f'Wrong answer: {result}'
    result = quick_sort([33, 55, -1, -2, -3, 64])
    assert result == [-3, -2, -1, 33, 55, 64], f'Wrong answer: {result}'
    result = quick_sort([0])
    assert result == [0], f'Wrong answer: {result}'
    result = quick_sort([1, 2, 3])
    assert result == [1, 2, 3], f'Wrong answer: {result}'
    result = quick_sort([-33, 0, -32, 1, -30, 2])
    assert result == [-33, -32, -30, 0, 1, 2], f'Wrong answer: {result}'
    test_name = traceback.extract_stack()[-2].line
    print(f'{test_name}: Все тесты пройдены!')


def test_determine_winners():
    result = determine_winners([
        ['alla', '4', '100'],
        ['gena', '6', '1000'],
        ['gosha', '2', '90'],
        ['rita', '2', '90'],
        ['timofey', '4', '80'],
    ])
    assert result == 'gena\ntimofey\nalla\ngosha\nrita', (
        f'Wrong answer: {result}'
    )
    result = determine_winners([
        ['b', '0', '1000'],
        ['c', '4', '2000'],
        ['d', '3', '90'],
        ['e', '4', '500'],
        ['gg', '4', '500'],
    ])
    assert result == 'e\ngg\nc\nd\nb', f'Wrong answer: {result}'
    result = determine_winners([
        ['b', '5', '10'],
        ['a', '2', '20'],
        ['g', '2', '0'],
        ['b', '0', '500'],
        ['a', '4', '500'],
    ])
    assert result == 'b\na\ng\na\nb', f'Wrong answer: {result}'
    result = determine_winners([
        ['b', '5', '10'],
    ])
    assert result == 'b', f'Wrong answer: {result}'
    test_name = traceback.extract_stack()[-2].line
    print(f'{test_name}: Все тесты пройдены!')


if __name__ == '__main__':
    # test_quick_sort()
    # test_determine_winners()
    count = int(input())
    array = [input().split() for _ in range(count)]
    print(determine_winners(array))
