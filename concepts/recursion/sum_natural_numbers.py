def sum_of_natural_numbers_recursive(start, sum):
    if (start < 1):
        return print(sum)
    sum_of_natural_numbers_recursive(start - 1, sum + start)

sum_of_natural_numbers_recursive(3, 0)