import heapq

def kth_max_element(arr, k):
    """
    Finds the kth largest element in the given array using a max heap.

    Parameters:
    arr (List): A list of integers from which the kth largest element needs to be found.
    k (int): The position of the largest element to find.

    Returns:
    int: The kth largest element in the array.

    Time complexity: O(nlogk), where n is the length of the input array.
    Space complexity: O(k), where k is the position of the largest element to find.
    """
    heapq.heapify(arr)
    
    for _ in range(k - 1):
        heapq.heappop(arr)
        
    return -heapq.heappop(arr)   
    
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_max_element(arr, k))