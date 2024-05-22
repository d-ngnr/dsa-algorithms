def kth_min_element(arr, k):
    arr.sort()
    return arr[k - 1]

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_min_element(arr, k))