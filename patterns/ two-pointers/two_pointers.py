# Pattern 1: Traversing from both ends
# Problem: Given a sorted array, find if there exists a pair that sums to target

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
            right - 1
    return False