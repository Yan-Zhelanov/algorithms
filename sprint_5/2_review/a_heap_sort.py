# 59602974

"""
    --- Принцип работы ---
Для начала сделаем наш массив кучей, для этого будем искать самые большие
элементы с середины массива, потому что веток у других элементов нет, так как,
если умножить их индекс на двойку, то мы выйдем за размер массива. Далее будем
для нулевого индекса искать самый большой элемент в массиве, после будем
менять его местами с последним неотсортированным местом в массиве, запускать
повторно поиск самого большого элемента, не проверяя при этом последние
отсортированные элементы.

    --- Доказательство корректности ---
Из описания следует, что мы будем находить самый большой элемент в массиве, а
после ставить его в конец, эта операция будет повторяться, пока площадь поиска
не будет равна единице, тогда на нулевом элементе останется один элемент, его
сортировать не нужно, он уже самый маленький.

    --- Временная сложность ---
В худшем, среднем и лучшем случаях: O(n * log(n))

    --- Пространственная сложность ---
Реализация требует хранить три индекса, в худшем случае, когда поиск самого
большого элемента запущен с нулевого индекса и каждый раз будет происходить
перестановка, то-есть нахождение большего элемента, то в худшем случае, глубина
вызов будет log(n), таким образом в худшем случае: O(log(n) * 3) = O(log(n))
В лучшем случае: O(1)
В среднем случае: O(log(n))
"""

import traceback


def heapsort(array):
    def _heapify(array, index, size):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if left <= size and array[left] > array[largest]:
            largest = left
        if right <= size and array[right] > array[largest]:
            largest = right
        if index != largest:
            array[index], array[largest] = array[largest], array[index]
            _heapify(array, largest, size)

    size = len(array) - 1
    for index in range(size//2, 0, -1):
        _heapify(array, index, size)
    for index in range(size, 0, -1):
        _heapify(array, 0, index)
        array[0], array[index] = array[index], array[0]
    return array


def determine_winners(array, name=0, score=1, penalty=2):
    array = list(map(
        lambda participant: (
            -int(participant[score]),
            int(participant[penalty]),
            participant[name],
        ),
        array,
    ))
    heapsort(array)
    return '\n'.join(participant[2] for participant in array)


def test_heapsort():
    result = heapsort([-3, 10, 22, -5, 1, 2, 11, 10])
    assert result == [-5, -3, 1, 2, 10, 10, 11, 22], f'Wrong answer: {result}'
    result = heapsort([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5], f'Wrong answer: {result}'
    result = heapsort([10])
    assert result == [10], f'Wrong answer: {result}'
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
        ['alla', '0', '0'],
        ['gena', '0', '0'],
        ['gosha', '0', '0'],
        ['rita', '0', '0'],
        ['timofey', '0', '0'],
    ])
    assert result == 'alla\ngena\ngosha\nrita\ntimofey', (
        f'Wrong answer: {result}'
    )
    result = determine_winners([
        ['a', '0', '10'],
        ['b', '1', '10'],
        ['c', '3', '3000'],
        ['d', '0', '10'],
        ['e', '1', '20'],
    ])
    assert result == 'c\nb\ne\na\nd', f'Wrong answer: {result}'
    test_name = traceback.extract_stack()[-2].line
    print(f'{test_name}: Все тесты пройдены!')


if __name__ == '__main__':
    # test_heapsort()
    # test_determine_winners()
    count = int(input())
    array = [input().split() for _ in range(count)]
    print(determine_winners(array))
