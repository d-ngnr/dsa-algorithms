def countDigits(n):
    while n != 0:
        n = n // 10 # This will remove the last digit for every iteration
        count += 1
    return count

# Example usage
n = 12345
print(countDigits(n))