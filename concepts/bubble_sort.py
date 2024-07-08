def bubble_sort(unordered_list):
    size = len(unordered_list)
    for i in range(size):
        for j in range(0, size - i - 1):
            if unordered_list[j] > unordered_list[j + 1]:
                unordered_list[j], unordered_list[j + 1] = unordered_list[j + 1], unordered_list[j]

    return unordered_list

# Example usage
unordered_list = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(unordered_list)) # Output: [11, 12, 22, 25, 34, 64, 90]