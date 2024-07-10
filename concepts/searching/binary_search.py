def binary_search(needle, haystack):
    """
    This will only work if the array or list is sorted ascendingly.
    """
    left = 0
    right = len(haystack) - 1
    while left <= right:
        mid = (left + right) // 2
        if haystack[mid] == needle:
            return mid
        elif haystack[mid] < needle:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
haystack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
needle = 5
result = binary_search(needle, haystack)
print(result)