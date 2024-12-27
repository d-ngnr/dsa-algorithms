# Pattern 1: Fixed Window Size
# Problem: Find maximum sum of any contiguous subarray of size k

def max_sum_of_subarray(arr, k):
    if len(arr) == 0:
        return None
    
    # Calculate some of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide window and update max_sum
    for i in range(k, len(arr)):
        window_sum = window_sum + arr[i] - arr[i - k] # always subtract the previous start of the window
        max_sum = max(max_sum, window_sum) # get the larger max_sum value
    
    return max_sum

# Example usage
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(max_sum_of_subarray(arr, k))