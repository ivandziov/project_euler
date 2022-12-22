from math import sqrt


def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(limit)) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes


def get_sum_primes_to_limit(limit):
    primes = sieve(limit)
    return sum(i for i in range(2, limit + 1) if primes[i])


test_limit = 2_000_000
print(get_sum_primes_to_limit(test_limit))
