import random

def partition(arr, left, right):
    # Choose a random pivot index between left and right
    pivot_index = random.randint(left, right)
    pivot = arr[pivot_index]
    # Move pivot to the end of the array
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left
    # Iterate over the array and partition
    for i in range(left, right):
        # If the current element is greater than the pivot, move it to the store_index
        if arr[i] > pivot:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    # Move the pivot to its final place
    arr[store_index], arr[right] = arr[right], arr[store_index]
    return store_index

def quickselect(arr, left, right, k):
    # Base case: the list contains only one element
    if left == right:
        return arr[left]
    
    # Partition the array and get the pivot index
    pivot_index = partition(arr, left, right)
    
    # If the pivot index is the k-th element, return it
    if k == pivot_index:
        return arr[k]
    # If k is less than the pivot index, recur on the left sub-array
    elif k < pivot_index:
        return quickselect(arr, left, pivot_index - 1, k)
    # If k is greater than the pivot index, recur on the right sub-array
    else:
        return quickselect(arr, pivot_index + 1, right, k)

def kth_max_element_quickselect(arr, k):
    # The Kth largest element is the (len(arr) - k)-th smallest element
    return quickselect(arr, 0, len(arr) - 1, len(arr) - k)

# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_max_element_quickselect(arr, k))  # Output: 10
