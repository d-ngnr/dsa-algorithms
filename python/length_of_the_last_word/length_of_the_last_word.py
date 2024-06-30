def lengthOfLastWord(s: str) -> int:
    """
    Finds the length of the last word in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The length of the last word in the string.

    Time complexity: O(n), where n is the length of the input string.
    Space complexity: O(1), as no extra space is used.
    """
    # Initialize variables
    i = len(s) - 1
    j = len(s) - 1
    last_word = True

    # Traverse the string from the end
    while i >= 0:
        # If the current character is a space
        if s[i] == " ":
            # If the last word has ended
            if last_word:
                # Decrement the index
                j = i
            last_word = True
        else:
            last_word = False
        i -= 1
        
# Example usage
s = "Hello World"
print(lengthOfLastWord(s))  # Output: 5