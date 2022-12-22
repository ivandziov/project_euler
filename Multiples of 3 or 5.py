def solution(number):
    return sum(
        [
            number for number in range(1, number)
            if (number % 3) == 0
            or (number % 5) == 0
        ]
    )


test_sequence = 1000
print(solution(test_sequence))
