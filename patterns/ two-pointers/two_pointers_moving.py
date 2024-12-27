# Pattern 2: Two pointers moving in same direction
# Problem: Remove duplicates from sorted array in-place
def remove_duplicates(arr):
    if not arr:
        return 0
    
    # slow pointer keeps track of where to place next unique element
    slow = 1
    
    for fast in range(1, len(arr)):
        if arr[fast] != arr[fast - 1]:
            arr[slow] = arr[fast]
            slow += 1
            
    return slow # length of array with duplicates removed

arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
new_length = remove_duplicates(arr)
print(new_length)
    
    