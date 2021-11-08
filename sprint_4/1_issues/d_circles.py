def determine_circles(array):
    result = {}
    for item in array:
        result[item] = result.get(item, True)
    return '\n'.join(result.keys())


def test_determine_circles():
    result = determine_circles([
        'вышивание крестиком',
        'рисование мелками на парте',
        'настольный керлинг',
        'настольный керлинг',
        'кухня африканского племени ужасмай',
        'тяжелая атлетика',
        'таракановедение',
        'таракановедение',
    ])
    assert result == (
        'вышивание крестиком\nрисование мелками на парте\nнастольный керлинг'
        '\nкухня африканского племени ужасмай\nтяжелая атлетика'
        '\nтаракановедение'
    ), f'Wrong answer: {result}'
    result = determine_circles(['у', 'ф', 'ф', 'б', 'ф', 'б', 'е', 'ф', 'у'])
    assert result == 'у\nф\nб\nе', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_circles()
    count = int(input())
    array = [input() for _ in range(count)]
    print(determine_circles(array))
