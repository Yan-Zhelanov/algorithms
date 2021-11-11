def determine_max_size_of_substring(text):
    result = [0]
    substring = []
    for char in text:
        if char in substring:
            substring = substring[substring.index(char)+1:] + [char]
            result.append(len(substring))
            continue
        substring.append(char)
        result[-1] += 1
    return max(result) if len(result) > 1 else result[-1]


def test_determine_max_size_of_substring():
    result = determine_max_size_of_substring('abcabcbb')
    assert result == 3, f'Wrong answer: {result}'
    result = determine_max_size_of_substring('aaawsdasdwertg')
    assert result == 8, f'Wrong answer: {result}'
    result = determine_max_size_of_substring('abcsssdewasssss')
    assert result == 5, f'Wrong answer: {result}'
    result = determine_max_size_of_substring('abcde')
    assert result == 5, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_max_size_of_substring()
    print(determine_max_size_of_substring(input()))
