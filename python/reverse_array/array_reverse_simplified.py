def simplified_reverse_array(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end="")
        if i != 0:
            print(" ", end="")
    print()  # Add a newline at the end of the function
        
original_array = [1,2,3,4,5,6,7,8,9]
simplified_reverse_array(original_array)