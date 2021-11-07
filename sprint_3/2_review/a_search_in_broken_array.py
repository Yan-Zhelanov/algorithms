# 56006146

"""
    --- Принцип работы ---
В начале мы запускаем двоичный поиск "разрыва" массива. Будем считать разрывом
тот элемент, после которого идёт меньший элемент. Такой элемент может быть в
массиве только один, либо, если массив не сломан, такого элемента просто не
будет, в таком случае поиск вернёт -1. Для начала определим индекс центрального
элемента, для этого сложим левый и правый края, в начале они будут равны 0 и
n-1, соответственно, где n — длинна массива, сумму поделим нацело на 2.
Проверим, если индекс левого края меньше центра, значит проверим больше ли
предыдущий от центрального элемента самого центрального элемента, если да, то
это и есть разрыв. Если нет, то проверим, что индекс правого края больше
центра, тогда проверим, что центральный элемент больше следующего, если это
так, то центральный элемент — это разрыв. Если нет, тогда мы сравниваем
значение левого элемнта с центральным, если левый элемент больше центрального,
тогда левая часть массива сломана, в ней и будем искать дальше разрыв. Если
наоборот, то правая часть массива сломана и поиск производить будем уже в ней.
Таким образом, если разрыв не найден, мы просто запускаем бинарный поиск по
массиву, иначе мы проверяем, что разрыв это искомый элемент. Если это не так,
мы определяем какому из двух отрезков принадлежит искомый элемент и запускаем
бинарный поиск внутри этого отрезка.

    --- Доказательство корректности ---
Из описания следует, что если разрыв будет найден, то мы сможем определить два
не сломанных участка массива. По значениям границ определить какому конкретно
участку принадлежит наш элемент, а после попробовать найти нужный элемент в
нём.

    --- Временная сложность ---
Поиск разрыва будет занимать O(log(n)), где n — длинна массива, после будет
запущен ещё один поиск, который в худшем случае будет занимать O(log(n-2)), так
как, если разрыв существует, в худшем случае он поделит массив на участки
размером 1 и n-1, но мы проверяем сам разрыв и поэтому исключаем его из
большего отрезка, в итоге отрезок получается размером n-2.
Итого: O(log(n)) + O(log(n-2)) = O(log(n))

    --- Пространственная сложность ---
Данная реализация требует хранение индексов левой и правой границ, а так же
центрального элемента, эти три переменные занимают фиксированный объём памяти.
Итого: O(1).
"""

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
