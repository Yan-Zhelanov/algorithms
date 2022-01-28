# 64596794

"""
    --- Принцип работы ---
Создадим префиксное дерево, следующие вершины префиксного дерева будем хранить
в словаре, чтобы их можно было быстро искать, терминальные узлы будем отмечать
длиной самого слова, чтобы позже эту длину можно было отнять. После создания
дерева создадим массив, куда будем записывать промежуточные решения: можно ли
создать строку с данным индексом или нет? На нулевом индексе распологается
пустая строка, поэтому её можно создать, запишем в неё положительный ответ.
Далее для каждого индекса будем проходиться по префиксному дереву, до тех пор
пока буквы совпадают или мы не превысим длинну самой строки. Если мы встречаем
терминальный узел и при этом, если ответ положительный и для строки без
текущего рассматриваемого слова, мы записываем положительный ответ в текущую
ячейку, иначе оставляем отрицательный.

    --- Доказательство корректности ---
Из описания следует, что для каждого индекса строки мы проверим все возможные
узлы префиксного дерева и если мы будем встречать терминальные узлы, мы будем
отмечать в массиве положительные ответы только в том случае, если строку без
терминального слова мы можем получить так же из слов в нашем префиксном дереве.
Отсюда следует, что если есть такая комбинация слов из которой мы можем
получить всю строку, мы её получим и отметим это в последней ячейке нашего
массива.

    --- Временная сложность ---
Для создания дерева нам потребуется: O(k), где k — суммарная длина всех слов во
множестве. Далее для каждого индекса мы будем запускать поиск по префиксному
дереву, в лучшем случае поиск будет останавливаться сразу же: O(n),
где n — количество символов в строке. В среднем случае так же будет: O(n),
а в худшем случае, если для каждого индекса мы будем проходить полностью по
префиксному дереву, а дерево будет длиною n: O(n^2).
Итого,
В худшем случае: O(k + n^2) = O(n^2)
В среднем и лучшем случаях: O(k + n) = O(n)

   --- Пространственная сложность ---
Для хранения дерева нам понадобиться хранить узлы, для каждого узла нам нужно
хранить значение, словарь и терминальное значение, в лучшем случае, если все
слова имеют один корень: O(n * 3), где n — суммарная длина всех слов во
множестве. В худщем случае, если все слова имеют разные корни: O(n * k * 3),
где n — количество слов, а k — средняя длина слов. А также нам потребуется
хранить массив с промежуточными решениями для каждого индекса: O(l),
где l — количество символов в строке. А также нужно хранить два индекса и
ссылку на следующий узел: O(3).
Итого,
В худшем и среднем случаях: O(n * k * 3 + l + 3) = O(n)
В лучшем случае: O(n * 3 + l + 3) = O(n)
"""


class Node:
    def __init__(self, value, nexts=None):
        self.value = value
        self.nexts = {} if nexts is None else nexts
        self.terminal = False


def get_tree(words):
    root = Node('')
    for word in words:
        node = root
        for index, char in enumerate(word):
            new_node = Node(char)
            node.nexts[char] = node.nexts.get(char, new_node)
            if index == len(word) - 1:
                node.nexts[char].terminal = len(word)
            node = node.nexts[char]
    return root


def is_possible_to_split(string, words):
    root = get_tree(words)
    dp = [False] * (len(string)+1)
    dp[0] = True
    node = root
    for index in range(len(string)):
        subindex = 0
        while index + subindex < len(string) + 1:
            if node.terminal and dp[index+subindex-node.terminal]:
                dp[index+subindex] = True
            if (
                index + subindex == len(string) or
                not node.nexts.get(string[index+subindex], False)
            ):
                node = root
                break
            node = node.nexts[string[index+subindex]]
            subindex += 1
    return 'YES' if dp[-1] else 'NO'


def test_is_possible_to_split():
    result = is_possible_to_split('runandrun', ['run', 'and'])
    assert result == 'YES'
    result = is_possible_to_split('aaa', ['a'])
    assert result == 'YES'
    result = is_possible_to_split('aaa', ['b'])
    assert result == 'NO'
    result = is_possible_to_split('acab', ['ac', 'a', 'b'])
    assert result == 'YES'
    result = is_possible_to_split('acab', ['ac', 'a', 'c'])
    assert result == 'NO'
    result = is_possible_to_split('abababa', ['aba'])
    assert result == 'NO'
    result = is_possible_to_split('abaab', ['aba'])
    assert result == 'NO'
    result = is_possible_to_split('abaab', ['abaa', 'aba', 'ab'])
    assert result == 'YES'
    print('All tests passed!')


if __name__ == '__main__':
    # test_is_possible_to_split()
    print(
        is_possible_to_split(input(), [input() for _ in range(int(input()))])
    )
