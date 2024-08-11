def reverse_digits(digits):
    reverseNum = 0
    
    while digits > 0:
        lastDigit = digits % 10                         # get the remainder of the digit
        reverseNum = (reverseNum * 10) + lastDigit      # construct the reverse number starting from the last digit
        digits = digits // 10                           # get the latest digit after removing the last one
    
    return reverseNum

print(reverse_digits(12345));
        