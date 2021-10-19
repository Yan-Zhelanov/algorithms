def get_y(a, x, b, c):
    return a * x * x + b * x + c

def test_get_y():
    assert get_y(-8, -5, -2, 7) == -183
    assert get_y(8, 2, 9, -10) == 40
    print('Тесты успешно пройдены!')

if __name__ == '__main__':
    print(get_y(*map(int, input().split())))
