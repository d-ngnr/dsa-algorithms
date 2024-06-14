def kth_max_element(arr, k):
    """
    Finds the kth largest element in the given array using sorting.

    Parameters:
    arr (List): A list of integers from which the kth largest element needs to be found.
    k (int): The position of the largest element to find.

    Returns:
    int: The kth largest element in the array.

    Time complexity: O(nlogn), where n is the length of the input array.
    Space complexity: O(1), as no extra space is used.
    """
    return arr[-1 - (k - 1)]

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_max_element(arr, k))