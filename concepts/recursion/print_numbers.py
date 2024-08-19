def print_numbers(number):
    if number > 0:
        print_numbers(number - 1)
        print(number, end=" ")

print_numbers(5)