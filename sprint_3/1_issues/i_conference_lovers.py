def determine_best_university(ids, count):
    id_counts = {}
    for id in ids:
        id_counts[id] = id_counts.get(id, 0) + 1
    id_counts = dict(
        sorted(id_counts.items(), key=lambda item: (-item[1], item[0]))
    )
    result = []
    for id in id_counts.keys():
        result.append(int(id))
        if len(result) == count:
            break
    return ' '.join(str(num) for num in result)


def test_determine_best_university():
    result = determine_best_university(['1', '2', '3', '1', '2', '3', '4'], 3)
    assert result == '1 2 3', f'Wrong answer: {result}'
    result = determine_best_university(['1', '2', '2', '4'], 1)
    assert result == '2', f'Wrong answer: {result}'
    result = determine_best_university(['5', '4', '4', '4'], 2)
    assert result == '4 5', f'Wrong answer: {result}'
    result = determine_best_university(['1'], 1)
    assert result == '1', f'Wrong answer: {result}'
    result = determine_best_university(['1', '1', '1', '2', '3', '3', '3'], 2)
    assert result == '1 3', f'Wrong answer: {result}'
    result = determine_best_university(['4', '4', '5', '5', '5', '3', '3'], 3)
    assert result == '5 3 4', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_best_university()
    input()
    print(determine_best_university(input().split(), int(input())))
