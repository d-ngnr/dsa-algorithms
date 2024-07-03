def jump_to_end(arr):
    """
    Determines if it is possible to reach the end of the given array by jumping from one index to another.

    Parameters:
        arr (List[int]): The input array.

    Returns:
        bool: True if it is possible to reach the end of the array, False otherwise.
    """
    for i in range(len(arr) - 1):               # start from the first element
        if arr[i] >= i + 1:                     # if the element is greater than or equal to the index
            if i + arr[i] >= len(arr) - 1:      # if the index plus the element is greater than or equal to the last element
                return True                     # return True
        else:
            return False                        # return False

# Example usage
arr = [2, 3, 1, 1, 4]
print(jump_to_end(arr))  # Output: True

arr = [3, 2, 1, 0, 4]
print(jump_to_end(arr))  # Output: False