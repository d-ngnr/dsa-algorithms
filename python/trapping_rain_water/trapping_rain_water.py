def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = 0, len(height) - 1
    max_left, max_right = height[left], height[right]
    total = 0
    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(max_left, height[left])
            total += max_left - height[left]
        else:
            right -= 1
            max_right = max(max_right, height[right])
            total += max_right - height[right]
    return total

# Example usage
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))  # Output: 6