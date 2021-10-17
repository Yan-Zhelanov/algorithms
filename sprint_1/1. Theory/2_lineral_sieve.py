def get_prime_numbers(before):
    least_prime_divisors = [0] * (before + 1)
    primes = []
    for index in range(2, before + 1):
        if least_prime_divisors[index] == 0:
            least_prime_divisors[index] = index
            primes.append(index)
        for prime in primes:
            composite = prime * index
            if (prime > least_prime_divisors[index]) or (composite > before):
                break
            least_prime_divisors[composite] = prime
    return primes


if __name__ == '__main__':
    print(get_prime_numbers(100))
