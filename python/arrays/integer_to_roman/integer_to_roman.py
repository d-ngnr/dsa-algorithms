def intToRoman(number):
    """
    Given an integer, convert it to a roman numeral.

    Parameters:
    number (int): The integer to be converted.

    Returns:
    str: The roman numeral representation of the input integer.

    Time complexity: O(n), where n is the number of characters in the roman numeral representation.
    Space complexity: O(1), as only constant extra space is used.
    """
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    result = ''
    for value in roman:
        while number >= value:
            result += roman[value]
            number -= value
    return result

# Example usage:
print(intToRoman(1994)) # Output: "MCMXCIV"