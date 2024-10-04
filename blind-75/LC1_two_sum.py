def two_sum(nums, target):
    prevValues = {}
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevValues:
            return [prevValues[diff], i]
        prevValues[n] = i
        
# Example usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target)) # Output: [1, 2]