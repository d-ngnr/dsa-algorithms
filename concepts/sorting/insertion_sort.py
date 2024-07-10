def insertion_sort(unordered_list):
    """
    Sorts an unordered list using the insertion sort algorithm.

    Parameters:
    - unordered_list (list): The list to be sorted.

    Returns:
    - list: The sorted list in ascending order.

    Time complexity: O(n^2), where n is the number of elements in the list.
    Space complexity: O(1), as no extra space is used.
    """
    for i in range(1, len(unordered_list)):
        j = i
        while j > 0 and unordered_list[j] < unordered_list[j - 1]:
            unordered_list[j], unordered_list[j - 1] = unordered_list[j - 1], unordered_list[j]
            j -= 1
    return unordered_list

# Example usage:
unordered_list = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(unordered_list)) # Output: [11, 12, 22, 25, 34, 64, 90]