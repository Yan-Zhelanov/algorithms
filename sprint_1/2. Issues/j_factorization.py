# def get_primes(before):
#     least_primes = [0] * (before + 1)
#     primes = []
#     for index in range(2, before+1):
#         if least_primes[index] == 0:
#             primes.append(index)
#         for prime in primes:
#             if prime * index > before:
#                 break
#             least_primes[prime*index] = prime
#     return primes


def factorize(number):
    i = 2
    result = ''
    source = number
    while i <= source:
        if number % i == 0:
            result += f'{i} '
            number //= i
            continue
        i += 1
    return result
        


# def test_primes():
#     result = get_primes(10)
#     assert result == [2, 3, 5, 7], (
#         f'Wrong answer: {result}'
#     )
#     result = get_primes(30)
#     assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], (
#         f'Wrong answer: {result}'
#     )
#     print('Все тесты пройдены!')


def test_factorize():
    result = factorize(8)
    assert result == '2 2 2 ', f'Wrong answer: {result}'
    result = factorize(13)
    assert result == '13 ', f'Wrong answer: {result}'
    result = factorize(100)
    assert result == '2 2 5 5 ', f'Wrong answer: {result}'
    result = factorize(84)
    assert result == '2 2 3 7 ', f'Wrong answer: {result}'
    result = factorize(2)
    assert result == '2 ', f'Wrong answer: {result}'
    result = factorize(794897)
    assert result == '73 10889 ', f'Wrong answer: {result}'
    result = factorize(794897)
    assert result == '73 10889 ', f'Wrong answer: {result}'
    result = factorize(862399)
    assert result == '862399 ', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_primes()
    test_factorize()
    # print(factorize(int(input())))
