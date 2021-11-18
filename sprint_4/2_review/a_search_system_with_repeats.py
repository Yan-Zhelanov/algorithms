def search(docs, requests):
    docs_words = {}
    repeats = {}
    index = 0
    while index < len(docs):
        if docs[index] in docs[:index]:
            previous = docs[:index].index(docs[index])
            repeats[previous] = repeats.get(previous, []) + [index]
            index += 1
            continue
        for word in docs[index].split():
            docs_words[word] = docs_words.get(word, {})
            docs_words[word][index] = docs_words[word].get(index, 0) + 1
        index += 1
    scores = []
    for index in range(len(requests)):
        scores.append({})
        for word in set(requests[index].split()):
            if word not in docs_words:
                continue
            for doc_index, count in docs_words[word].items():
                scores[index][doc_index] = (
                    scores[index].get(doc_index, 0) + count
                )
    result = {}
    for index in range(len(scores)):
        for item in sorted(
            scores[index].items(), key=lambda item: (-item[1], item[0])
        ):
            if item[1] <= 0:
                continue
            result[index] = result.get(index, []) + [item[0]+1]
            if item[0] in repeats:
                result[index] += [index+1 for index in repeats[item[0]]]
    return '\n'.join(
        ' '.join(str(index) for index in element[:5])
        for element in result.values() if len(element) > 0
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
    # result = search(
    #     [
    #         'one two', 'two two', 'one two', 'two two',
    #     ],
    #     [
    #         'three', 'two', 'two two', 'one', 'one two', 'one two two'
    #     ],
    # )
    # assert result == '2 4 1 3\n2 4 1 3\n1 3\n1 2 3 4\n1 2 3 4', (
    #     f'Wrong answer: {result}'
    # )
    result = search(
        [
            'i love ice-cream', 'i love coffee',
        ],
        [
            'ice-cream coffee coffee',
        ],
    )
    assert result == '1 2', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_search()
    count = int(input())
    docs = [input() for _ in range(count)]
    count = int(input())
    requests = [input() for _ in range(count)]
    print(search(docs, requests))
