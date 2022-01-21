# 64227535

"""
    --- Принцип работы ---
В массиве будем хранить промежуточные результаты вычислений разниц между двумя
строками. Нулевой индекс обозначает пустую строку, поэтому самый первый элемент
будет имень значение 0, так как между пустой строкой и другой пустой строкой
разницы никакой нет. Между пустой строкой и какой-либо строкой разница будет
равна количеству символов в непустой строке, так как чтобы из пустой строки
получить любую непустую строку, нужно добавить в пустую каждый символ из
непустой. Чтобы посчитать разницу дальше, нужно понять равны ли текущие символы
или нет. Если они не равны, то разница равна единице, в противном случае нулю.
Если прибавить эту разницу к разнице предыдущего шага, когда в обоих строках
было меньше на один символ мы получим один из возможных ответов для текущих
положений строк. Другие два возможных варианта это когда к меньшей строке мы
добавляем недостающий элемент, или из большей строки удаляем лишний элемент,
для этого нужно взять разницу между строками, одна из которых будет меньше
другой и прибавить к этой разнице единицу. Минимальный из этих трёх вариантов
и будет ответ на подзадачу.

    --- Доказательство корректности ---
Из описания следует, что каждую итерацию будет высчитываться разница между
двумя подстроками. Есть несколько возможных вариантов получить из одной строки
другую, если строки одинаковой длинны, можно просто заменить неравные символы,
если строки разной длинны, можно добавить в меньшую строку нехватающих символов
или удалить из большей строки лишние символы. Каждую итерацию будут просчитаны
все возможные варианты и выбран самый короткий путь, что и требуется по условию
задачи.

    --- Временная сложность ---
В худшем, среднем и лучшем случаях: O((N+1) * (M+1)), где N — длина первой
строки, а M — длина второй строки, единица добавляется так как мы каждую строку
сравниваем с пустой строкой.
Итого: O(N * M)

   --- Пространственная сложность ---
Потребуется хранить два массива с промежуточными результатами, каждую итерацию
также может высчитываться одна переменная, отсюда следует, что в худшем,
среднем и лучшем случаях: O((N+1) * 2 + 1), где N — размер меньшей из двух
строк.
Итого: O(N)
"""


def determine_levenstein_distance(string_1, string_2):
    if len(string_1) > len(string_2):
        string_1, string_2 = string_2, string_1
    dp = [[0] * (len(string_1)+1) for _ in range(2)]
    for i in range(len(string_2)+1):
        for j in range(len(string_1)+1):
            if i == 0:
                dp[1][j] = j
                continue
            if j == 0:
                dp[1][j] = i
                continue
            action = 0
            if string_2[i-1] != string_1[j-1]:
                action = 1
            dp[1][j] = min(dp[0][j]+1, dp[1][j-1]+1, dp[0][j-1]+action)
        dp[0] = list(dp[1])
    return dp[-1][-1]


def test_determine_levenstein_distance():
    result = determine_levenstein_distance('queue', 'ueue')
    assert result == 1, f'Wrong answer: {result}'
    result = determine_levenstein_distance('abacaba', 'abaabc')
    assert result == 2, f'Wrong answer: {result}'
    result = determine_levenstein_distance('innokentiy', 'innnokkentia')
    assert result == 3, f'Wrong answer: {result}'
    result = determine_levenstein_distance('qeeq', 'uuiq')
    assert result == 3, f'Wrong answer: {result}'
    result = determine_levenstein_distance('qeep', 'uuiq')
    assert result == 4, f'Wrong answer: {result}'
    result = determine_levenstein_distance('r', 'x')
    assert result == 1, f'Wrong answer: {result}'
    result = determine_levenstein_distance('q', 'q')
    assert result == 0, f'Wrong answer: {result}'
    result = determine_levenstein_distance('', 'x')
    assert result == 1, f'Wrong answer: {result}'
    result = determine_levenstein_distance('', '')
    assert result == 0, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_determine_levenstein_distance()
    print(determine_levenstein_distance(input(), input()))
