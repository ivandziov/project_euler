from math import sqrt


def find_max_prime_number(number):
    max_prime_number = 0

    while number % 2 == 0:
        max_prime_number = 2
        number /= 2

    for i in range(3, int(sqrt(number)) + 1, 2):
        while number % i == 0:
            max_prime_number = i
            number /= i

    if number > 2:
        max_prime_number = number

    return max_prime_number


test_number = 600851475143
print(find_max_prime_number(test_number))
