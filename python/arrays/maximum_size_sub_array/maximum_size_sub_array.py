def max_sub_array(arr, k):
    """
    Finds the maximum size sub-array of length k in the given array.

    Parameters:
    arr (List): A list of integers.
    k (int): The length of the sub-array.

    Returns:
    int: The maximum size sub-array of length k in the array.

    Time complexity: O(n), where n is the length of the input array.
    Space complexity: O(1), as no extra space is used.
    """
    if not arr or k <= 0 or k > len(arr):
        return 0;                           # Return if constraints are not met
    
    window_sum = sum(arr[:k])               # Initialize window sum based on size
    max_sum = window_sum                    # Equate maximum to window sum changing values
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example usage
arr = [1, 2, 3, 4, 5]
k = 2
print(max_sub_array(arr, k))  # Output: 7