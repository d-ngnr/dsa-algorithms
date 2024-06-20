def max_profit_stocks_p2(arr):
    """
    Calculates the maximum profit that can be achieved by buying and selling stocks twice.

    Args:
        arr (List[int]): A list of integers representing the prices of stocks.

    Returns:
        int: The maximum profit that can be achieved by buying and selling stocks twice.

    Time complexity: O(n), where n is the length of the input array.
    Space complexity: O(1), as no extra space is used.

    The function iterates through the input array and calculates the profit by subtracting the previous price from the current price.
    The maximum profit is returned at the end of the function.

    Example:
        >>> max_profit_stocks_p2([7, 1, 5, 3, 6, 4])
        7
    """
    
    for i in range(1, len(arr)):                # start from the second element
        if arr[i] > arr[i-1]:                   # if the current element is greater than the previous element
            total_profit += arr[i] - arr[i-1]   # add the profit
            
    return total_profit                         # return the total profit

# Example usage
arr = [7, 1, 5, 3, 6, 4]
print(max_profit_stocks_p2(arr)) # Output: 7