def factorize(number):
    divider = 2
    result = []
    source = number ** 0.5
    while divider <= source:
        if number % divider == 0:
            result.append(divider)
            number //= divider
            continue
        divider += 1
    if number != 1:
        result.append(number)
    return ' '.join(str(num) for num in result)


def test_factorize():
    result = factorize(8)
    assert result == '2 2 2', f'Wrong answer: {result}'
    result = factorize(13)
    assert result == '13', f'Wrong answer: {result}'
    result = factorize(100)
    assert result == '2 2 5 5', f'Wrong answer: {result}'
    result = factorize(84)
    assert result == '2 2 3 7', f'Wrong answer: {result}'
    result = factorize(2)
    assert result == '2', f'Wrong answer: {result}'
    result = factorize(794897)
    assert result == '73 10889', f'Wrong answer: {result}'
    result = factorize(794897)
    assert result == '73 10889', f'Wrong answer: {result}'
    result = factorize(862399)
    assert result == '862399', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    # test_factorize()
    print(factorize(int(input())))
