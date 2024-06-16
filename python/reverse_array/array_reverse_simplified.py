def simplified_reverse_array(arr):
    """
    Reverses the given array by printing its elements in reverse order.

    Parameters:
        arr (list): The array to be reversed.

    Returns:
        None

    Time complexity: O(n), where n is the length of the input array.
    Space complexity: O(1), as only constant extra space is used.
    """
    for i in range(len(arr), -1, -1): # Iterate from the last element to the first
        print(arr[i], end="")
        if i != 0:
            print(" ", end="")
    print()  # Add a newline at the end of the function
        
original_array = [1,2,3,4,5,6,7,8,9]
simplified_reverse_array(original_array)