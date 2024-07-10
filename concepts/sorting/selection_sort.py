def selection_sort(unordered_list):
    """
    Sorts an unordered list using the selection sort algorithm.

    Parameters:
    - unordered_list (list): The list to be sorted.

    Returns:
    - list: The sorted list in ascending order.

    Time complexity: O(n^2), where n is the number of elements in the list.
    Space complexity: O(1), as no extra space is used.
    """
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