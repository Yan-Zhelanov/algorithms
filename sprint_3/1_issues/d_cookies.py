def determine_happy_childs(childs, cookies):
    childs.sort()
    cookies.sort()
    result = 0
    index = 0
    for child in childs:
        while index < len(cookies) and child > cookies[index]:
            index += 1
        if index == len(cookies):
            break
        index += 1
        result += 1
    return result


def test_determine_happy_childs():
    result = determine_happy_childs([1, 2], [2, 1, 3])
    assert result == 2, f'Wrong answer: {result}'
    result = determine_happy_childs([2, 4], [1, 1, 2])
    assert result == 1, f'Wrong answer: {result}'
    result = determine_happy_childs([5, 4], [1, 1, 2])
    assert result == 0, f'Wrong answer: {result}'
    result = determine_happy_childs([4], [1, 1, 2])
    assert result == 0, f'Wrong answer: {result}'
    result = determine_happy_childs([5], [5])
    assert result == 1, f'Wrong answer: {result}'
    result = determine_happy_childs([1, 2, 2, 3, 5], [1, 2, 4, 5])
    assert result == 4, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_happy_childs()
    input()
    childs = list(map(int, input().split()))
    input()
    cookies = list(map(int, input().split()))
    print(determine_happy_childs(childs, cookies))
