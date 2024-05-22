def kth_max_element(arr, k):
    arr.sort()
    return arr[-1 - (k - 1)]

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_max_element(arr, k))