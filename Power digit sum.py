def get_power_digit_sum(number):
    return sum(map(int, str(number)))


test_number = 2 ** 1000
print(get_power_digit_sum(test_number))