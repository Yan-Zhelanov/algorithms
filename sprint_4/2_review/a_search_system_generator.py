def search(docs, requests):
    docs_words = {}
    repeats = {}
    for index in range(len(docs)):
        if docs[index] in docs[:index]:
            previous = docs[:index].index(docs[index])
            repeats[previous] = repeats.get(previous, []) + [index]
            continue
        for word in docs[index].split():
            docs_words[word] = docs_words.get(word, {})
            docs_words[word][index] = docs_words[word].get(index, 0) + 1
    result = []
    for request_index in range(len(requests)):
        result.append({})
        for word in set(requests[request_index].split()):
            if word in docs_words:
                for index, count in docs_words[word].items():
                    result[request_index][index] = (
                        result[request_index].get(index, 0) + count
                    )
    result = [
        [
            (_index for _index in [[item[0]] + repeats[item[0]]][:5])
            if item[0] in repeats
            else item[0]
            for item in sorted(
                result[index].items(), key=lambda item: (-item[1], item[0])
            )[:5] if item[1] > 0
        ] for index in range(len(result))
    ]
    return '\n'.join(
        ' '.join(
            str(index+1)
            if 
            for index in element[:5]
        )
        for element in result
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
    test_search()
    count = int(input())
    docs = [input() for _ in range(count)]
    count = int(input())
    requests = [input() for _ in range(count)]
    print(search(docs, requests))
