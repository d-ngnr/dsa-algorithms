def sum_of_natural_numbers(number):
    sum = 0
    
    for i in range(1, number + 1):
        sum += i
    return sum

def sum_of_natural_numbers_p2(number):
    return int(number * (number + 1) / 2)
    

print(sum_of_natural_numbers(5))
print(sum_of_natural_numbers_p2(5))