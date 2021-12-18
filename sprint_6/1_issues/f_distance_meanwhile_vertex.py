def determine_min_dist(count, array, start, end):
    graph = [[] for _ in range(count)]
    for line in array:
        if len(line) != 2:
            continue
        left, right = int(line[0])-1, int(line[1])-1
        graph[left].append(right)
        graph[right].append(left)


def test_determine_min_dist():
    result = determine_min_dist(5, [
        ['2', '4'],
        ['3', '5'],
        ['2', '1'],
        ['2', '3'],
        ['4', '5'],
    ], '1', '5')
    assert result == 3, f'Wrong answer: {result}'
    result = determine_min_dist(4, [
        ['2', '3'],
        ['4', '3'],
        ['2', '4'],
    ], '1', '3')
    assert result == -1, f'Wrong answer: {result}'
    result = determine_min_dist(2, [
        ['2', '1'],
    ], '1', '1')
    assert result == 1, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_determine_min_dist()
