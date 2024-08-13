def is_armstrong(number):
    # An Armstrong number is a number that is equal to the sum of its 
    # own digits each raised to the power of the number of digits
    # Sample: 3, 153 = 1^3 + 5^3 + 3^3
    
    k = len(str(number))                # get the length of the number
    sum = 0                             # initiate the sum to zero
    tempNumber = number                 # save the original number to a temp variable
    
    while tempNumber > 0:               # Iterate until the temp variable is zero
        lastDigit = tempNumber % 10     # get the last digit
        sum += lastDigit ** k           # Raise the last digit to the kth power 
        tempNumber = tempNumber // 10   # Remove the last digit from the temp variable
    return sum == number                # check if the sum is equal to the original number

# Example
print(is_armstrong(153))