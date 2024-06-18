def simplified_reverse_array(arr):
    # starts with last element and ends with the first element with a step of -1
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end="")
        if i != 0:
            print(" ", end="")
    print()  # Add a newline at the end of the function
        
original_array = [1,2,3,4,5,6,7,8,9]
simplified_reverse_array(original_array) # Output: 9 8 7 6 5 4 3 2 1