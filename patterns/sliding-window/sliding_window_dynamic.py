# Pattern 2: Dynamic Window Size
# Problem: Find longest subarray with sum less than or equal to target

def longest_subarray_sum(arr, target):
    window_sum = 0
    window_start = 0
    max_length = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        # Shrink window while sum is too large
        while window_sum > target and window_start <= window_end:
            window_sum -= arr[window_start]
            window_start += 1
            
        # Update max_length if current window is valid
        max_length = max(max_length, window_end - window_start + 1)
        
    return max_length

# Example usage:
arr = [1, 2, 3, 4, 5]
target = 10
print(longest_subarray_sum(arr, target))