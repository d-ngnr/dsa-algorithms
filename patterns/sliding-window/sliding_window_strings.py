# Pattern 3: String Pattern Matching
# Problem: Find all anagrams of pattern in string

def find_anagrams(s, pattern):
    # Edge case check
    if len(pattern) > len(s):
        return []
    
    pattern_freq = {}   # Will store frequency of chars in pattern
    window_freq = {}    # Will store frequency of chars in current window
    result = []        # Will store starting indices of anagrams
    
    # Count frequency of each char in pattern
    # For pattern = "abc":
    # pattern_freq = {'a': 1, 'b': 1, 'c': 1}
    for char in pattern:
        pattern_freq[char] = pattern_freq.get(char, 0) + 1
        
    # Count frequency of chars in first window
    # For s = "cbaebabacd", pattern length = 3:
    # First window is "cba"
    # window_freq = {'c': 1, 'b': 1, 'a': 1}
    for i in range(len(pattern)):
        char = s[i]
        window_freq[char] = window_freq.get(char, 0) + 1
        
    # If frequencies match, we found an anagram
    # In our example, "cba" is an anagram of "abc"
    # result = [0]
    if window_freq == pattern_freq:
        result.append(0)
        
    for i in range(len(pattern), len(s)):
        # Remove leftmost char of previous window
        old_char = s[i - len(pattern)]
        window_freq[old_char] -= 1
        if window_freq[old_char] == 0:
            del window_freq[old_char]
        
        # Add new char to window
        new_char = s[i]
        window_freq[new_char] = window_freq.get(new_char, 0) + 1
        
        # Check if current window is an anagram
        if window_freq == pattern_freq:
            result.append(i - len(pattern) + 1)
            
    return result

# Example usage
s = "cbaebabacd"
pattern = "abc"
print(find_anagrams(s, pattern))