def sortedSquares(nums):
    """
    Given an integer array nums sorted in non-decreasing order, 
    return an array of the squares of each number sorted in non-decreasing order.
    
    Example:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].
    """
    n = len(nums)
    left = 0
    right = n - 1
    result = [0] * n
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
    return result

# Example usage
nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums)) # Output: [0, 1, 9, 16, 100]