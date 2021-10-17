def get_prime_numbers(before):
    primes = [num for num in range(before)]
    primes[0] = primes[1] = False
    for num in range(2, before):
        if primes[num]:
            for index in range(num*num, before, num):
                primes[index] = False
    return primes


if __name__ == '__main__':
    print(get_prime_numbers(100))
