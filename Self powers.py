def get_last_ten_digits(number):
    total = 0
    for i in range(1, number + 1):
        total += i ** i
    return str(total)[-10:]


test_number = 1000
print(get_last_ten_digits(test_number))
