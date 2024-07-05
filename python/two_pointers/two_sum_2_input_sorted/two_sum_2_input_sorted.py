def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            return [left + 1, right + 1]
        
# Example usage:
numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target)) # Output: [1, 2]
