def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    if sum(gas) < sum(cost):            # if the sum of gas is less than the sum of cost
        return -1                       # return -1
    start = 0                           # start from the first element
    total = 0                           # initialize the total
    for i in range(len(gas)):           # iterate over the array
        total += gas[i] - cost[i]       # update the total
        if total < 0:                   # if the total is less than 0
            start = i + 1               # update the start
            total = 0                   # reset the total
    return start                        # return the start

# Example usage
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas, cost))    # Output: 3