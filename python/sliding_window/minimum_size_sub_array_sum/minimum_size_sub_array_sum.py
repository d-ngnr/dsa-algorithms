def minSubArray(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    left = 0
    current_sum = 0
    min_size = len(nums) + 1
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_size = min(min_size, right - left + 1)
            current_sum -= nums[left]
            left += 1
    return min_size if min_size != len(nums) + 1 else 0

# Example usage
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArray(target, nums)) # Output: 2