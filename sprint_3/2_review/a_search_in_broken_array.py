# 56268438

"""
    --- Принцип работы ---
Каждую итерацию будем разбивать массив на две половинки, так как разрыв в
массиве может быть только один, по условиям задачи, будем определять, какая из
половинок не сломана. Проверим, лежит ли искомое число между границ правильной
половинки, если лежит, то поиск продолжим в ней, а если нет, будем искать в
другой половинке.

    --- Доказательство корректности ---
Из описания следует, что каждую итерацию мы будем делить массив на пополам и
продолжать поиски в той половинке, которая может содержать искомое число, пока
число не будет найдено. Если границы половинок пересекуться, а число не будет
найдено, будет возвращена -1.

    --- Временная сложность ---
Каждая итерация будет делить массив на пополам, поэтому даже если искомого
элемента нет в массиве, массив будет разделён log(n) раз в худшем случае.
В лучшем случае, если искомый элемент — это центральный, левая или правая
граница, выполнится всего одна итерация: O(1).
Из вышеописанного следует, что в среднем алгоритм работает за: O(log(n))

    --- Пространственная сложность ---
Данная реализация требует хранение индексов левой и правой границ, а так же
центрального элемента, эти три переменные занимают фиксированный объём памяти.
Итого: O(1).
"""


def broken_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        if array[left] == target:
            return left
        if array[right] == target:
            return right
        if array[left] <= array[middle]:
            if array[left] < target < array[middle]:
                right = middle - 1
            else:
                left = middle + 1
        elif array[middle] <= array[right]:
            if array[middle] < target < array[right]:
                left = middle + 1
            else:
                right = middle - 1
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
    assert result == -1, f'Wrong answer: {result}'
    result = broken_search([5, 6, 7, 8, 9, 0, 1, 2, 3, 4], 0)
    assert result == 5, f'Wrong answer: {result}'
    result = broken_search([1], 1)
    assert result == 0, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_broken_search()
