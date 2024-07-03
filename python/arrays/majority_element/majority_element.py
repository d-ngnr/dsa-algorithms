def majority_element(arr):
    """
    Finds the majority element in an array.

    Args:
        arr (List[int]): The input array.

    Returns:
        int: The majority element.

    Time complexity: O(n), where n is the length of the input array.
    Space complexity: O(1), as only constant extra space is used.

    The majority element is the element that appears more than half of the time in the array.

    The algorithm iterates through the array and keeps track of the current majority element and its count.
    If the current element is equal to the majority element, the count is incremented.
    If the current element is not equal to the majority element, the count is decremented.
    The majority element is returned at the end of the function.

    Example:
        >>> majority_element([2, 2, 1, 1, 1, 2, 2])
        2
    """
    majority = 0                    # initialize the majority element   
    count = 0                       # initialize the count
    for i in range(len(arr)):       # start from the first element
        if count == 0:              # if the count is zero
            majority = arr[i]       # update the majority element
        if arr[i] == majority:      # if the current element is equal to the majority element
            count += 1              # increment the count
        else:                       
            count -= 1              # decrement the count
    return majority

arr=[2,2,1,1,1,2,2]
print(majority_element(arr)) # Output: 2