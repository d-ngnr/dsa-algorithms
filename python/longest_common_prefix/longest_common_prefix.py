def longestCommonPrefix(self, prefix):
    """
    :type strs: List[str]
    :rtype: str
    """
    for i in range(len(prefix[0])):
        for s in prefix:
            if i == len(s) or s[i] != prefix[0][i]:
                return prefix[0][:i]
    return prefix[0]

# Example usage
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))