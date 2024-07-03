def candy(ratings):
    n = len(ratings)
    candy = [1 for i in range(n)]

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candy[i] = candy[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candy[i] = max(candy[i], candy[i + 1] + 1)

    return sum(candy)

# Example usage
ratings = [1, 0, 2]
print(candy(ratings))  # Output: 5