# Given an array of sorted numbers, 
# move all non-duplicate number instances at the beginning of the array 
# in-place. The non-duplicate numbers should be sorted and you should 
# not use any extra space so that the solution has 
# constant space complexity i.e., .

# Move all the unique number instances at the beginning of 
# the array and after moving return the length of the subarray 
# that has no duplicate in it.

def get_all_non_duplicates(array):
    if not array: 
        return 0
    
    slow = 1
    
    for fast in range(1, len(array)):
        if array[fast] != array[fast - 1]: # compare current and previous values
            array[slow] = array[fast]
            slow += 1
            
    return slow

arr = [2, 3, 3, 3, 6, 9, 9]
print(get_all_non_duplicates(arr))