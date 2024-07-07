def lengthOfLongestSubstringKDistinct(s, k):
    """
    Finds the length of the longest substring of a string with at most k distinct characters.

    Parameters:
    s (str): The input string.
    k (int): The maximum number of distinct characters allowed in the substring.

    Returns:
    int: The length of the longest substring with at most k distinct characters.

    Time complexity: O(n), where n is the length of the input string.
    Space complexity: O(1), as no extra space is used.
    """
    # Initialize variables
    i = 0
    j = 0
    max_length = 0
    char_frequency = {}

    # Traverse the string and find the length of the longest substring with at most k distinct characters
    while j < len(s):
        if s[j] not in char_frequency:
            char_frequency[s[j]] = 0
        char_frequency[s[j]] += 1
        if len(char_frequency) <= k:
            max_length = max(max_length, j - i + 1)
        else:
            while len(char_frequency) > k:
                char_frequency[s[i]] -= 1
                if char_frequency[s[i]] == 0:
                    del char_frequency[s[i]]
                i += 1
        j += 1
    return max_length

# Example usage
s = "araaci"
k = 2
print(lengthOfLongestSubstringKDistinct(s, k))  # Output: 4