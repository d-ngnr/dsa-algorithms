def reverse_array_using_stack(arr):
    stack = []
    
    for element in arr:
        stack.append(element)
    
    # pop elements from stack and assign it to the array indices
    for i in range(len(arr)):
        arr[i] = stack.pop() # pop gets the last element from the stack
        
original_array = [1,2,3,4,5,6,7,8,9]
reverse_array_using_stack(original_array)
[print(a, end=" ") for a in original_array]
print()