# Given an array of numbers sorted in ascending order and a target sum, 
# find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair)
# such that they add up to the given target. 
# If no such pair exists return [-1, -1].

def find_indices_of_sum(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]

nums = [1, 2, 3, 4, 6]
target = 6
print(find_indices_of_sum(nums, target))