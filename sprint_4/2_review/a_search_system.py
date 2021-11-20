# 58730285

"""
    --- Принцип работы ---
Заведём словарь, в нём будем хранить слова, которые встречаются нам в
документах, с количеством повторений каждого слова для каждого из документов.
Далее, будем перебирать для каждого поискового запроса уникальные слова. Если
слово встречается в словаре, который мы завели ранее, то мы запишем все индексы
которые есть в словаре под этим словом, если индекс уже записан, мы просто
добавим к сумме этого индекса количество повторений нового слова и таким
образом мы будем обновлять итоговые суммы индексов, пока в запросе не
закончатся слова. После отсортируем полученные результаты для запроса, и будем
выводить индексы, пока не выведем 5 или индексы не закончатся.

    --- Доказательство корректности ---
Из описания следует, что каждый раз, когда мы будем встречать слово в запросе,
которое записанно у нас в словаре, мы будем выписывать все индексы из словаря
или добавлять к сумме уже имеющегося индекса количество повторений нового
слова. Таким образом, для каждого запроса мы получим итоговую сумму для
каждого уникального документа.

    --- Временная сложность ---
В начале мы считаем количество слов в каждом документе: каждую итерацию мы
будем проходить по всем документам длинной n, а для каждого документа
проходить по всем словам, предположим, что количество слов в среднем k, итого:
O(n*k). Далее, мы пройдём по каждому слову в каждом запросе, а для каждого
найденого слова в словаре мы пройдёмся по всем его индексам, итого в среднем:
O(c*f*g), где c — это количество запросов, f — это количество слов в каждом
запросе, а g — это посчитанные ранее индексы для слова. Наконец, для каждого
запроса мы находим 5 самых релевантных документов, итого в среднем: O(c*5)
Если всё это объединить, то получим: O(n*k + c*f*n*k + c*5) = O(n)

    --- Пространственная сложность ---
Данная реализация требует хранение слов и индексов документов с количеством
повторений: O(n*k*2), где n — количество слов, k — индексы документов в которых
встречаются эти слова, к тому же k умножается на 2, потому что для каждого
индекса нужно хранить ещё и количество повторений.
Так же, для каждого запроса мы будем считать итоговую сумму для каждого из
встречающихся индексов: O(g*2), где g — это посчитанные ранее индексы, так как
для каждого индекса нам нужно хранить ещё и итоговую сумму, то мы умножаем g на
два.
Итого: O(n*k*2 + g*2) = O(n)
"""


def search(docs, requests):
    def _get_words(words, docs):
        for index in range(len(docs)):
            for word in docs[index].split():
                words[word] = words.get(word, {})
                words[word][index] = words[word].get(index, 0) + 1

    def _get_score(request, words):
        result = {}
        for word in set(request.split()):
            if word not in words:
                continue
            for index, count in words[word].items():
                result[index] = result.get(index, 0) + count
        for index, _ in sorted(
            result.items(), key=lambda item: (-item[1], item[0])
        )[:5]:
            print(index+1, end=' ')
        print()

    words = {}
    _get_words(words, docs)
    for request in requests:
        _get_score(request, words)


def test_search():
    result = search(
        [
            'i love coffee', 'coffee with milk and sugar',
            'free tea for everyone',
        ],
        [
            'i like black coffee without milk', 'everyone loves new year',
            'mary likes black coffee without milk',
        ],
    )
    assert result == '1 2\n3\n2 1', f'Wrong answer: {result}'
    result = search(
        [
            'buy flat in moscow', 'rent flat in moscow', 'sell flat in moscow',
            'want flat in moscow like crazy',
            'clean flat in moscow on weekends', 'renovate flat in moscow',
        ],
        [
            'flat in moscow for crazy weekends', 'flat', 'flat in',
        ],
    )
    assert result == '4 5 1 2 3\n1 2 3 4 5\n1 2 3 4 5', (
        f'Wrong answer: {result}'
    )
    result = search(
        [
            'buy flat in moscow', 'rent flat in moscow', 'sell flat in moscow',
            'want flat in moscow like crazy',
            'clean flat in moscow on weekends', 'renovate flat in moscow',
        ],
        [
            'flat in moscow for crazy weekends', 'flat', 'flat in',
        ],
    )
    assert result == '4 5 1 2 3\n1 2 3 4 5\n1 2 3 4 5', (
        f'Wrong answer: {result}'
    )
    result = search(
        [
            'i love ice-cream', 'i love coffee',
        ],
        [
            'ice-cream coffee coffee',
        ],
    )
    assert result == '1 2', f'Wrong answer: {result}'
    result = search(
        [
            'i am copy paste', 'i am copy paste', 'i am copy paste',
            'i am copy paste', 'i am copy paste', 'i am copy paste',
        ],
        [
            'copy paste',
        ],
    )
    assert result == '1 2 3 4 5', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_search()
    count = int(input())
    docs = [input() for _ in range(count)]
    count = int(input())
    requests = [input() for _ in range(count)]
    search(docs, requests)
