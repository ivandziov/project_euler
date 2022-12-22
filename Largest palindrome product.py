def is_palindrome(number):
    reversed_number = str(number)[::-1]
    return str(number) == reversed_number


def find_max_palindrome(start, end):
    max_palindrome = 0

    for i in range(end, start - 1, -1):
        for j in range(end, start - 1, -1):
            if i * j > max_palindrome:
                if is_palindrome(i * j) and (i * j) > max_palindrome:
                    max_palindrome = i * j
                    break
                elif i * j < max_palindrome:
                    break

    return max_palindrome


test_start = 100
test_end = 999

print(find_max_palindrome(test_start, test_end))


