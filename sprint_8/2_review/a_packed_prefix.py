# 64635163

"""
    --- Принцип работы ---
Будем распаковывать строки согласно простым правилам: если встречается символ,
а перед ним не было скобок и цифр, мы добавим этот символ к результату, если
же нам встречается число и квадратные скобки, то мы запишем число в стек
множителей и запишем все символы в скобках в стек со словами к последнему
слову. Если встречается закрывающая скобка, то мы последнее слово в стеке
умножим на последний множитель в другом стеке, если в стеке со словами не
осталось больше слов, то мы добавим полученное слово к результату, а если в
стеке ещё лежат слова, то мы добавим полученное слово к последнему слову в
стеке. Префиксы будем считать посимвольно, возьмём самую маленькую строчку из
всех и пройдёмся по каждому её символу, каждый символ будем сверять с символами
на тех же местах у других строк, как только мы найдём хотя бы одно расхождение,
мы найдём индекс конца префикса.

    --- Доказательство корректности ---
Из описания следует, что скобки мы будем расскрывать последовательно,
внутренние выражения будут добавленные к внешним, так будет происходить до тех
пор, пока внешних выражений не останется, тогда полученная строка будет
добавленна к результату, а если строка не была закончена, то все действия по
раскрытию скобок повторятся. Также, из описания следует, что префикс будет
найден по символам наименьшей строки, если расхождение не будет найдено, то
будет возвращена наименьшая строка, так как только она может быть самым
наибольшим общим префиксом, в противном случае, будет возвращена часть строки
до индекса, не включая его самого, где было найдено расхождение, что и
требуется по условиям задачи.

    --- Временная сложность ---
На распаковку каждой строки мы потратим O(n), где n — количество символов в
строке. На распаковку всех строк в лучшем случае, если строка всего одна: O(n),
а в худшем случае, если строк n или большее количество: O(n^2). После мы
потратим O(k), где k — количество элементов в массиве, для поиска минимального
элемента в массиве. В лучшем случае, если элемент будет всего один: O(1). Далее
мы будем сверять каждый символ минимальной строки с символами остальных строк:
O(n^2), а в лучшем случае, если строка всего одна сразу же её вернём: O(1).
Итого,
В худшем и среднем случае: O(n^2 + k + n^2) = O(n^2)
В лучшем случае: O(n)

   --- Пространственная сложность ---
Нам потребуется хранить O(n) распакованных элементов, где n — количество строк,
в худшем случае, а в лучшем O(1), если строка всего одна. Ещё понадобится
хранить один символ и минимальный индекс для ответа: O(2).
Итого,
В худшем и среднем случае: O(n + 2) = O(n)
В лучшем случае: O(1)
"""


def unpack(string):
    multipliers = []
    words = []
    result = []
    for char in string:
        if char.isnumeric():
            multipliers.append(int(char))
            continue
        if char == '[':
            words.append([])
            continue
        if char == ']':
            if len(words) == 1:
                result.append(''.join(words.pop()) * multipliers.pop())
                continue
            previous = ''.join(words.pop())
            words[-1].append(previous * multipliers.pop())
            continue
        if len(words) == 0:
            result.append(char)
            continue
        words[-1].append(char)
    return ''.join(result)


def unpack_strings(strings):
    result = []
    for string in strings:
        result.append(unpack(string))
    return result


def get_max_prefix(strings):
    strings = unpack_strings(strings)
    if len(strings) == 1:
        return strings[0]
    min_index = strings.index(min(strings))
    for index in range(len(strings[min_index])):
        symbol = strings[0][index]
        for string in strings[1:]:
            if symbol != string[index]:
                return string[:index]
    return strings[min_index]


def test_unpack():
    result = unpack('kek')
    assert result == 'kek', f'Wrong answer: {result}'
    result = unpack('2[kek]')
    assert result == 'kekkek', f'Wrong answer: {result}'
    result = unpack('2[k2[j]]')
    assert result == 'kjjkjj', f'Wrong answer: {result}'
    result = unpack('1[k2[j3[l]]]')
    assert result == 'kjllljlll', f'Wrong answer: {result}'
    result = unpack_strings(['1[la]4[k]', '2[te]2[st]', '2[e2[k2[l]]]'])
    assert result == ['lakkkk', 'tetestst', 'ekllkllekllkll'], (
        f'Wrong answer: {result}'
    )
    print('Unpack tests passed!')


def test_get_max_prefix():
    result = get_max_prefix(['1[la]4[k]', '2[te]2[st]', '2[e2[k2[l]]]'])
    assert result == '', f'Wrong answer: {result}'
    result = get_max_prefix(['1[g2[p]]', '2[gp]2[st]', '2[gp2[gp2[g]]]'])
    assert result == 'gp', f'Wrong answer: {result}'
    result = get_max_prefix(['3[gpp]', 'g2[p]2[g2[p]]', '2[g2[p]]'])
    assert result == 'gppgpp', f'Wrong answer: {result}'
    result = get_max_prefix(['3[gpp]'])
    assert result == 'gppgppgpp', f'Wrong answer: {result}'
    print('Get max prefix tests passed!')


if __name__ == '__main__':
    # test_unpack()
    # test_get_max_prefix()
    print(get_max_prefix([input() for _ in range(int(input()))]))
