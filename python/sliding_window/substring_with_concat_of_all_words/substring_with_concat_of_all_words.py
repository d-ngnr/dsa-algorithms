def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    if not s or not words:
        return []

    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    word_len = len(words[0])
    window = len(words) * word_len

    res = []    
    for i in range(len(s) - window + 1):
        word_map = {}
        for j in range(i, i + window, word_len):
            word = s[j:j + word_len]
            if word not in word_freq:
                break
            if word not in word_map:
                word_map[word] = 1
            else:
                word_map[word] += 1
            if word_map[word] > word_freq[word]:
                break
            if j + word_len == i + window:
                res.append(i)
    return res
    
# Example usage
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words))  # Output: [0, 9]