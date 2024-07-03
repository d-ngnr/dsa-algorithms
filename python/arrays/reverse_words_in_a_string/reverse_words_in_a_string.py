def reverseWords(words):
    """
    Reverses the order of the words in a string.

    Args:
        words (str): A string containing multiple words.

    Returns:
        str: The string with the words in reverse order.

    Time complexity: O(n), where n is the length of the input string.
    Space complexity: O(n), where n is the length of the input string.
    """
    return ' '.join(words.split()[::-1])

# Example usage
words = "the sky is blue"
print(reverseWords(words))  # Output: "blue is sky the"