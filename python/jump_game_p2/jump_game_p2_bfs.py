def jump_p2_bfs(arr):
    result = 0
    l = r = 0
    
    while r < len(arr) - 1:
        furthest = 0
        for i in range(l, r + 1):
            furthest += max(furthest, i + arr[i])
        l = r + 1
        r = furthest
        result += 1

    return result

# Example usage
arr = [2, 3, 1, 1, 4]
print(jump_p2_bfs(arr))  # Output: 2

arr = [3, 2, 1, 0, 4]
print(jump_p2_bfs(arr))  # Output: 2