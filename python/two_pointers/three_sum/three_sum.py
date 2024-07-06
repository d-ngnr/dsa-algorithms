def three_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    triplets = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1
    return triplets

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums)) # Output: [[-1,-1,2],[-1,0,1]]