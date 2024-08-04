import math

def countDigits(n):
    return int(math.log10(n) + 1)

# Example usage
n = 12345
print(countDigits(n))