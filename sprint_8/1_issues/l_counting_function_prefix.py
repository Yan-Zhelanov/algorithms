def get_prefixes(string):
    prefixes = [None] * len(string)
    prefixes[0] = 0
    for i in range(1, len(string)):
        k = prefixes[i-1]
        while k > 0 and string[i] != string[k]:
            k = prefixes[k-1]
        if string[i] == string[k]:
            k += 1
        prefixes[i] = k
    return ' '.join(str(prefix) for prefix in prefixes)


def test_get_prefixes():
    result = get_prefixes('ahaha')
    assert result == '0 0 1 2 3', f'Wrong answer: {result}'
    result = get_prefixes('abracadabra')
    assert result == '0 0 0 1 0 1 0 1 2 3 4', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_get_prefixes()
    print(get_prefixes(input()))
