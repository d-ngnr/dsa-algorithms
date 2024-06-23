def find_h_index(arr):
    """
    Finds the h-index of a researcher based on their citations.

    Args:
        arr (List[int]): The list of citations of the researcher.

    Returns:
        int: The h-index of the researcher.

    The h-index is a metric that measures both the productivity and citation impact of a researcher. 
    It is defined as the maximum value of h such that the researcher has published h papers that have each been cited at least h times.

    The function sorts the input array in ascending order, then iterates over the array to find the h-index.
    If the current element is greater than or equal to the number of elements left, it returns the h-index.
    If no element satisfies the condition, it returns 0.
    """
    arr.sort()
    n = len(arr)            # number of elements in the array
    
    for i in range(n):      # iterate over the array
        if arr[i] >= n - i: # if the array element is greater than or equal to the number of elements left
            return n - i    # return the number of elements left
    return 0                # return 0 if no element is greater than or equal to the number of elements left

# Example usage
arr = [3, 0, 6, 1, 5]
result = find_h_index(arr)
print(result)               # Output: 3