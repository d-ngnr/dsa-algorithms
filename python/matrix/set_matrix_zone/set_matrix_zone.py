def setZeroes(zeroes):
    """
    Do not return anything, modify matrix in-place instead.
    """
    for i in range(len(zeroes)):
        for j in range(len(zeroes[0])):
            if zeroes[i][j] == 0:
                for k in range(len(zeroes)):
                    if zeroes[k][j] != 0:
                        zeroes[k][j] = -1
                for k in range(len(zeroes[0])):
                    if zeroes[i][k] != 0:
                        zeroes[i][k] = -1
    for i in range(len(zeroes)):
        for j in range(len(zeroes[0])):
            if zeroes[i][j] == -1:
                zeroes[i][j] = 0

    return zeroes

# Example usage
zeroes = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(setZeroes(zeroes))