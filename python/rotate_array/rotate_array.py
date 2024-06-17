def rotate_array(arr, k):
    """
    Rotates the array by k positions to the right.

    Parameters:
    arr (list): A list of integers to be rotated.
    k (int): The number of positions to rotate the array.

    Returns:
    list: The rotated array.

    Time complexity: O(n), where n is the length of the input array.
    Space complexity: O(1), as only constant extra space is used.
    """
    n = len(arr)                              # length of the array
    k = k % n                                 
    for _ in range(k):                        # rotate the array k times  
        temp = arr[n - 1]                     # store the last element
        for i in range(n - 1, 0, -1):         # shift the elements to the right
            arr[i] = arr[i - 1]               # move the elements to the left
        arr[0] = temp                         # store the last element in the first index
    return arr                                # return the rotated array

nums = [1,2,3,4,5,6,7] 
k = 3
print(rotate_array(nums, k))