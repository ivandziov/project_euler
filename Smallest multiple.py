from functools import reduce
from math import gcd


def least_common_multiple(first_number, second_number):
    return first_number * second_number // gcd(first_number, second_number)


def solution(number):
    return reduce(least_common_multiple, range(1, number + 1))


test_sequence = 20
print(solution(test_sequence))
