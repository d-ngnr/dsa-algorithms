def check_duplicate(arr):
    hash_set = set()
    for num in arr:
        if num in hash_set:
            return True
        hash_set.add(num)
    return False

# Example usage
arr = [1, 2, 3, 1]
print(check_duplicate(arr))  # Output: True

