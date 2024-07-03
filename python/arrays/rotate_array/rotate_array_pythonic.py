def rotate_array_pythonic(arr, k):
    k = k % len(arr)
    arr[:] = arr[-k:] + arr[:-k]
    return arr

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_array_pythonic(arr, k))  # Output: [5, 6, 7, 1, 2, 3, 4]