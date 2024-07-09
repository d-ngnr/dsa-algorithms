def selection_sort(unordered_list):
    for i in range(len(unordered_list)):
        min_index = i
        for j in range(i + 1, len(unordered_list)):
            if unordered_list[j] < unordered_list[min_index]:
                min_index = j
        unordered_list[i], unordered_list[min_index] = unordered_list[min_index], unordered_list[i]
    return unordered_list

# Example usage
unordered_list = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(unordered_list)) # Output: [11, 12, 22, 25, 34, 64, 90]