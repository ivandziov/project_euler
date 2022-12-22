def get_sum_of_all_numbers(number, power):
    return sum(
        i for i in range(10, number)
        if i == sum(int(d) ** power for d in str(i))
    )


test_number = 1000000
print(get_sum_of_all_numbers(test_number, 5))
