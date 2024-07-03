def string_on_string(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    return haystack.find(needle)

# Example usage
haystack = "sadbutsad"
needle = "sad"
print(string_on_string(haystack, needle))  # Output: 0