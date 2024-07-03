def max_profit_stocks(arr):
    """
    Finds the maximum profit that can be earned by buying and selling stocks.

    Parameters:
        arr (list): A list of stock prices.

    Returns:
        int: The maximum profit that can be earned.

    Time complexity: O(n), where n is the length of the input array.
    Space complexity: O(1), as only constant extra space is used.
    """
    # Initialize variables
    min_price = arr[0]
    max_profit = 0

    # Iterate over the array
    for i in range(1, len(arr)):
        # Update the minimum price
        min_price = min(min_price, arr[i])
        # Update the maximum profit
        max_profit = max(max_profit, arr[i] - min_price)

    return max_profit

# Example usage
arr = [7, 1, 5, 3, 6, 4]
print(max_profit_stocks(arr)) # Output: 5