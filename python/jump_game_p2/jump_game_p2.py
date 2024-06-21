def jump_p2(arr):
    if len(arr) <= 1:
        return 0

    jumps = 0
    current_end = 0
    furthest = 0
    
    for i in range(len(arr) - 1):
        furthest = max(furthest, i + arr[i])
        if i == current_end:
            jumps += 1
            current_end = furthest
            
            if current_end >= len(arr) - 1:
                break
    return jumps

# Example usage
arr = [2, 3, 1, 1, 4]
print(jump_p2(arr))  # Output: 2

arr = [3, 2, 1, 0, 4]  
print(jump_p2(arr))  # Output: 2