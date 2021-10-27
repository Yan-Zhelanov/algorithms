# 55547980

"""
    --- Принцип работы ---
Создаём пустой массив в который будем складывать операнды и результаты
вычислений. Дальше будем перебирать поштучно каждый элемент данный нам.
Если этот элемент — операция, то проводим вычисления и кладём результат в
наш массив. Если это операнд, то просто положим его в массив.

    --- Доказательство корректности ---
Из описания следует, что самый последний элемент в массиве будет результат
последней операции, если операций было n-1, где n — количество операторов, то
в массиве будет лежать единственный элемент — ответ.

    --- Временная сложность ---
Если в массиве n элементов, то алгоритм выполнит n операци. Отсюда следует, что
алгоритм работает за O(n).

    --- Пространственная сложность ---
Чтобы перебрать каждый элемент по очереди, нам нужно хранить их все в массиве,
ещё мы храним промежуточные результаты в дополнительном массиве. Таким образом,
мы храним n элементов исходного массива и k элементов промежуточных
результатов. В итоге: O(n) + O(k) = O(n).
"""
import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


def calculate(array):
    result = []
    for item in array:
        if item in OPERATIONS:
            num_2, num_1 = result.pop(), result.pop()
            result.append(OPERATIONS[item](num_1, num_2))
            continue
        result.append(int(item))
    return result[-1]


def test_calculate():
    result = calculate(['2', '1', '+', '3', '*'])
    assert result == 9, f'Wrong answer: {result}'
    result = calculate(['9', '3', '/', '3', '-'])
    assert result == 0, f'Wrong answer: {result}'
    result = calculate(['12', '5', '/', '4', '+'])
    assert result == 6, f'Wrong answer: {result}'
    result = calculate(['12', '5', '/', '4', '+'])
    assert result == 6, f'Wrong answer: {result}'
    result = calculate(['12', '5', '4', '+', '*'])
    assert result == 108, f'Wrong answer: {result}'
    result = calculate(
        ['12', '4', '/', '10', '*', '5', '6', '13', '-', '+', '/']
    )
    assert result == -15, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_calculate()
    print(calculate(input().split()))
