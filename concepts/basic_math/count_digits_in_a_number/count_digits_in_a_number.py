def countDigits(n):
    count = 0
    while n != 0:
        count += 1
        n = n // 10 # This will remove the last digit for every iteration
    return count

# Example usage
n = 12345
print(countDigits(n))