def insert_strings(text, strings):
    strings = [
        [string, int(index)]
        for string, index in strings
    ]
    for string, current in strings:
        text = text[:current] + string + text[current:]
        length = len(string)
        for index in range(len(strings)):
            if current < strings[index][1]:
                strings[index][1] += length
    return text


def test_insert_strings():
    result = insert_strings('kukareku', [['p', '1'], ['q', '2']])
    assert result == 'kpuqkareku', f'Wrong answer: {result}'
    result = insert_strings('hello world', [['kek', '5'], ['kotik', '0']])
    assert result == 'kotikhellokek world', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_insert_strings()
    text = input()
    count = int(input())
    strings = [input().split() for _ in range(count)]
    print(insert_strings(text, strings))
