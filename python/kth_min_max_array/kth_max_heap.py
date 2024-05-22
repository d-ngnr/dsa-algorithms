import heapq

def kth_max_element(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    
    for _ in range(k - 1):
        heapq.heappop(arr)
        
    return -heapq.heappop(arr)   
    
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_max_element(arr, k))