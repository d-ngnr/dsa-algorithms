def quicksort(arr):
    """
    Sorts an array using the quicksort algorithm.

    Parameters:
        arr (list): The input list to be sorted.

    Returns:
        list: A sorted list in ascending order.

    Time complexity: O(n log(n)), where n is the length of the input list.
    Space complexity: O(log(n)), as only constant extra space is used.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print(sorted_arr)  # Output: [1, 5, 7, 8, 9, 10]