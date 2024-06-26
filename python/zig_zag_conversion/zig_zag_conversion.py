def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows <= 0 or numRows > len(s):
        return s
    L = [''] * numRows
    index, step = 0, 1
    for x in s:
        L[index] += x
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step
    return ''.join(L)

# Example usage
s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))