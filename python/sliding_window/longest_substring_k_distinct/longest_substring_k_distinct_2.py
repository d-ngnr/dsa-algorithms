from collections import defaultdict
def lengthOfLongestSubstringKDistinct(s, k):
    """
    Problem Statement:
    Given a string s and an integer k, find the length of the longest substring that contains at most k distinct characters.
    Example:
    Input: s = "aabacbebebe", k = 3
    Output: 7
    Explanation: The longest substring with at most 3 distinct characters is "cbebebe".
    """
    if not s or k == 0:
        return 0
    
    char_frequency = defaultdict(int)
    max_length = 0
    window_start = 0
    
    for window_end in range(len(s)):
        right_char = s[window_end]
        char_frequency[right_char] += 1
        
        while len(char_frequency) > k:
            left_char = s[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
            
        max_length = max(max_length, window_end - window_start + 1)
        
    return max_length

# Example usage
s = "aabacbebebe"
k = 3
print(lengthOfLongestSubstringKDistinct(s, k))  # Output: 7
    