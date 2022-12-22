def sum_of_squares(sequence):
    return sum(i ** 2 for i in sequence)


def square_of_sum(sequence):
    return sum(sequence) ** 2


def get_sum_square_difference(sequence):
    return abs(sum_of_squares(sequence) - square_of_sum(sequence))


test_sequence = range(1, 101)
print(get_sum_square_difference(test_sequence))
