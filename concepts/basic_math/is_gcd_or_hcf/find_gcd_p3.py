def find_gcd(num1, num2):
    while num1 > 0 and num2 > 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
            
    if num1 == 0:
        return num2
    return num1

print(find_gcd(20, 15))