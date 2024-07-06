def minWindow(s,t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if len(t) > len(s):
        return ""
    t_freq = {}
    for char in t:
        if char in t_freq:
            t_freq[char] += 1
        else:
            t_freq[char] = 1
    s_freq = {}
    left = 0
    right = 0
    start = 0
    min_len = len(s) + 1
    while right < len(s):
        char = s[right]
        if char in s_freq:
            s_freq[char] += 1
        else:
            s_freq[char] = 1
        if char in t_freq and s_freq[char] == t_freq[char]:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left
        right += 1
    return s[start:start+min_len]

# Example usage
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s,t))