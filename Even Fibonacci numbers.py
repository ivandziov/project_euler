def fib_even_sequence(number):
    n_first = 1
    n_second = 2
    even_numbers_sequence = [n_second]

    while n_second < number:
        n_second, n_first = n_second + n_first, n_second
        if n_second % 2 == 0:
            even_numbers_sequence.append(n_second)

    return even_numbers_sequence


def get_sum_of_even_numbers_in_fib_sequence(number):
    even_fib_numbers_sequence = fib_even_sequence(number)
    return sum(even_fib_numbers_sequence)


test_number = 4_000_000
print(get_sum_of_even_numbers_in_fib_sequence(test_number))
