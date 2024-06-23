def jump_p2(arr):
    """
    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length from that position.
    Your goal is to reach the last index in the minimum number of jumps.
    
    Parameters:
    arr (List[int]): A list of non-negative integers representing the maximum jump length from each position.
    
    Returns:
    int: The minimum number of jumps required to reach the last index.
    
    Time complexity: O(n), where n is the length of the input array.
    Space complexity: O(1), as only constant extra space is used.
    """

    if len(arr) <= 1:
        return 0

    jumps = 0                    # number of jumps
    current_end = 0              # current end of the jump
    furthest = 0                 # furthest position that can be reached
    
    for i in range(len(arr) - 1):               # start from the first element
        furthest = max(furthest, i + arr[i])    # update the furthest position
        if i == current_end:                    # if the current end is reached
            jumps += 1                          # increment the number of jumps
            current_end = furthest              # update the current end
            
            if current_end >= len(arr) - 1:     # if the current end is the last element
                break                           # break out of the loop
    return jumps                                # return the number of jumps

# Example usage
arr = [2, 3, 1, 1, 4]
print(jump_p2(arr))  # Output: 2

arr = [3, 2, 1, 0, 4]  
print(jump_p2(arr))  # Output: 2