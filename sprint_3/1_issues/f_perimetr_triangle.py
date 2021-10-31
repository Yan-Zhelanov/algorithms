def determine_max_perimetr_triangle(sides):
    sides.sort(key=lambda item: -item)
    index = 0
    while index < len(sides) - 2:
        next_sides = sides[index+1] + sides[index+2]
        if sides[index] < next_sides:
            return sides[index] + next_sides
        index += 1


def test_determine_max_perimetr_triangle():
    result = determine_max_perimetr_triangle([3, 3, 2, 6])
    assert result == 8, f'Wrong answer: {result}'
    result = determine_max_perimetr_triangle([8, 7, 14, 3])
    assert result == 29, f'Wrong answer: {result}'
    result = determine_max_perimetr_triangle([2, 2, 2, 4])
    assert result == 6, f'Wrong answer: {result}'
    result = determine_max_perimetr_triangle([1, 2, 3, 4, 5])
    assert result == 12, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_determine_max_perimetr_triangle()
    input()
    print(determine_max_perimetr_triangle(list(map(int, input().split()))))
