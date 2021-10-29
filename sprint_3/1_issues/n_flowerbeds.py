def determine_flowerbeds(array):
    array.sort()
    result = [array[0]]
    for flowerbed in array[1:]:
        if result[-1][1] >= flowerbed[0]:
            result[-1][0] = min(result[-1][0], flowerbed[0])
            result[-1][1] = max(result[-1][1], flowerbed[1])
            continue
        result.append(flowerbed)
    return '\n'.join(
        ' '.join(str(num) for num in flowerbed) for flowerbed in result
    )


def test_determine_flowerbeds():
    result = determine_flowerbeds([
        [2, 3], [5, 6], [3, 4], [3, 4]
    ])
    assert result == '2 4\n5 6', f'Wrong answer: {result}'
    result = determine_flowerbeds([
        [2, 3], [1, 2], [2, 3], [3, 4]
    ])
    assert result == '1 4', f'Wrong answer: {result}'
    result = determine_flowerbeds([
        [1, 3], [1, 3]
    ])
    assert result == '1 3', f'Wrong answer: {result}'
    result = determine_flowerbeds([
        [10, 33], [2, 3]
    ])
    assert result == '2 3\n10 33', f'Wrong answer: {result}'
    result = determine_flowerbeds([
        [6, 8], [6, 8], [1, 2], [4, 5], [3, 4], [2, 3], [5, 6]
    ])
    assert result == '1 8', f'Wrong answer: {result}'
    result = determine_flowerbeds([
        [4, 13], [48, 68], [42, 71], [6, 43], [17, 20], [43, 71], [42, 89],
        [20, 31], [0, 55]
    ])
    assert result == '0 89', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_flowerbeds()
    count = int(input())
    array = [list(map(int, input().split())) for _ in range(count)]
    print(determine_flowerbeds(array))
