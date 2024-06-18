def reverse_array_using_builtins(arr):
    [print(a, end=" ") for a in list(reversed(arr))]
    print() # removes the percent sign from the end of the string
    
original_array = [1,2,3,4,5,6,7,8,9]
reverse_array_using_builtins(original_array)    # Output: 9 8 7 6 5 4 3 2 1