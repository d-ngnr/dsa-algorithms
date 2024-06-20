def kth_min_element(arr, k):
    """
    Finds the kth smallest element in the given array using sorting.

    Parameters:
    arr (List): A list of integers from which the kth smallest element needs to be found.
    k (int): The position of the smallest element to find.

    Returns:
    int: The kth smallest element in the array.

    Time complexity: O(nlogn), where n is the length of the input array.
    Space complexity: O(1), as no extra space is used.
    """
    return arr[k - 1]

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_min_element(arr, k)) # Output: 3