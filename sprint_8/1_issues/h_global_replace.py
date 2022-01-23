def replace(string, pattern, to):
    result = string
    string = pattern + '#' + string
    prefixes = [None] * len(string)
    prefixes[0] = 0
    shift = 0
    for i in range(1, len(string)):
        k = prefixes[i-1]
        while k > 0 and string[i] != string[k]:
            k = prefixes[k-1]
        if string[i] == string[k]:
            k += 1
        prefixes[i] = k
        if k == len(pattern):
            result = (
                result[0:i-k-len(pattern)+shift]
                + to + result[i-len(pattern)+shift:]
            )
            shift += len(to) - k
    return result


def test_replace():
    result = replace('aaa', 'a', 'ab')
    assert result == 'ababab', f'Wrong answer: {result}'
    result = replace('maitkeit', 'it', '')
    assert result == 'make', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_replace()
    print(replace(input(), input(), input()))
