# 58674412

"""
    --- Принцип работы ---
Заведём два словаря, в первом будем хранить слова, которые встречаются нам в
документах, с количеством повторений каждого слова для каждого из документов.
Если документ нам встречался уже ранее, мы запишем его индекс во второй
словарь, где ключём будет индекс первого уникального такого документа. Далее,
будем перебирать для каждого поискового запроса уникальные слова. Если слово
встречается в словаре, который мы завели ранее, то мы запишем все индексы
которые есть в словаре под этим словом, если индекс уже записан, мы просто
добавим к сумме этого индекса количество повторений нового слова и таким
образом мы будем обновлять итоговые суммы индексов, пока в запросе не
закончатся слова. Заведём массив массивов для записи индексов по каждому
запросу. После отсортируем полученные результаты для каждого из запросов,
будем добавлять индексы пока размер подмассива не будет равен 5 или индексы
не закончатся. Также, после добавления индекса в подмассив будем проверять, не
встречается ли этот индекс в нашем словаре с повторениями, если встречается, то
будем выписывать из него индексы, пока подмассив удовлетворяет нашим условиям
или индексы не закончатся.

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
O(c*f*n*k), где c — это количество запросов, f — это количество слов в каждом
запросе, а n*k — это посчитанные ранее слова. Наконец, для каждого запроса мы
находим 5 самых релевантных документов, итого в среднем: O(c*5)
Если всё это объединить, то получим: O(n*k + c*f*n*k + c*5) = O(n)

    --- Пространственная сложность ---
Данная реализация требует хранение слов и индексов документов с количеством
повторений: O(n*k*2), где n — количество слов, k — индексы документов в которых
встречаются эти слова, к тому же k умножается на 2, потому что для каждого
индекса нужно хранить ещё и количество повторений.
Для хранения итоговых сумм для каждого запроса нам понадобится массив, в
котором будут лежать индексы и итоговые суммы к ним: O(c*k*2), где c —
количество запросов, k — индексы найденые раннее, а так же k снова умножается
на 2, потому что для каждого индекса нам нужно хранить ещё и итоговую сумму.
Для хранения результатов нам понадобится массив длинной c, где c — это
количество запросов, для каждого c искомых документов не может быть больше
пяти, отсюда следует: O(c*5)
Итого: O(n*k*2 + c*k*2 + c*5) = O(n)
"""


def search(docs, requests):
    words = {}
    repeats = {}
    for index in range(len(docs)):
        if docs[index] in docs[:index]:
            previous = docs[:index].index(docs[index])
            repeats[previous] = repeats.get(previous, []) + [index]
            continue
        for word in docs[index].split():
            words[word] = words.get(word, {})
            words[word][index] = words[word].get(index, 0) + 1
    scores = []
    for request_index in range(len(requests)):
        scores.append({})
        for word in set(requests[request_index].split()):
            if word not in words:
                continue
            for index, count in words[word].items():
                scores[request_index][index] = (
                    scores[request_index].get(index, 0) + count
                )
    result = []
    for request_index in range(len(scores)):
        result.append([])
        for index, _ in sorted(
            scores[request_index].items(),
            key=lambda item: (-item[1], item[0]),
        )[:5]:
            result[request_index].append(index+1)
            if index in repeats:
                for repeat_index in repeats[index][:4]:
                    if len(result[request_index]) < 5:
                        result[request_index].append(repeat_index+1)
                        continue
                    break
            if len(result[request_index]) >= 5:
                break
    return '\n'.join(
        ' '.join(str(index) for index in request)
        for request in result
    )


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
    print(search(docs, requests))
