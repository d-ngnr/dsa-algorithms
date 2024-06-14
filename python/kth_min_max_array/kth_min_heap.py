import heapq

def kth_min_element(arr, k):
    """
    Finds the kth smallest element in the given array using a min heap.

    Parameters:
    arr (List): A list of integers from which the kth smallest element needs to be found.
    k (int): The position of the smallest element to find.

    Returns:
    int: The kth smallest element in the array.

    Time complexity: O(nlogk), where n is the length of the input array.
    Space complexity: O(k), where k is the position of the smallest element to find.
    """
    
    for _ in range(k - 1):
        heapq.heappop(arr)
    
    return heapq.heappop(arr)

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_min_element(arr, k))