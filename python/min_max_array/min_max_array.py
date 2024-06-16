def get_min_max_value(arr):
    """
    Returns a list containing the minimum and maximum values in the given array.

    Parameters:
        arr (list): A list of integers.

    Returns:
        list: A list containing the minimum and maximum values in the given array.

    Time complexity: O(n), where n is the length of the input array.
    Space complexity: O(1), as only constant extra space is used.
    """
    return [min(arr), max(arr)]

original_array = {3, 2, 1, 56, 10000, 167}
[print(a, end=" ") for a in get_min_max_value(original_array)]
print()
