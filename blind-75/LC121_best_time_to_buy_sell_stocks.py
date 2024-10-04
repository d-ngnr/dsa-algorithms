def buy_sell_stocks(prices):
    min_price = prices[0]
    max_profit = 0
    
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    
    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print(buy_sell_stocks(prices))  # Output: 5