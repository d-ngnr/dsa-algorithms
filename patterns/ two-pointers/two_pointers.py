# Pattern 1: Traversing from both ends
# Problem: Given a sorted array, find if there exists a pair that sums to target

# Steps:
# 1. Initialize two pointers, one at the beginning and one at the end of the array
# 2. Move both pointers towards each other until they meet (while loop)
# 3. Check if the sum of the values at the pointers is equal to the target
# 4. Move both pointers in opposite directions until they meet again
def find_pair_sum(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            print(f'Found pair: {arr[left]}, {arr[right]}')
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return False

arr = [1, 2, 3, 4, 5, 6, 7]
target = 7
print(find_pair_sum(arr, target))