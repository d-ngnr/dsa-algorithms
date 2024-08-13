import math

def all_divisors(number):
    divisors = []
    for i in range(1, int(math.sqrt(number)) + 1):      # Iterate up to the square root of the number
        if (number % i == 0):                           # If no remainder, add it to the divisors list
            divisors.append(i)
            
            if i != number // i:                        
                divisors.append(number // i)            # Add the n/i into the divisors list
    return divisors

print(all_divisors(36))