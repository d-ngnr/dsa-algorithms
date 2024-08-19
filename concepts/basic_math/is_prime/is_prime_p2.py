import math

def is_prime(number):
    count = 0
    
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            count += 1
            
            if number // i != i:
                count += 1
    
    if count == 2:
        return True
    else:
        return False
    
print(is_prime(3))