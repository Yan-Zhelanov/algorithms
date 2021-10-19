def determine_the_winner(a, b, c):
    numbers = [a, b, c]
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return 'WIN' if len(even) == 0 or len(even) == 3 else 'FAIL'


def test_determine_the_winner():
    assert determine_the_winner(1, 2, -3) == 'FAIL'
    assert determine_the_winner(7, 11, 7) == 'WIN'
    assert determine_the_winner(6, -2, 0) == 'WIN'
    print('Тесты пройдены!')


if __name__ == '__main__':
    print(determine_the_winner(*map(int, input().split())))
