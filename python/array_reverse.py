def reverse_array_extra_array(arr):
    reversed_array = arr[::-1] # start from the end and move backwards
    
    print("Reversed array:", end=" ") # print without moving to the next line
    for i in reversed_array:
        print(i, end=" ")  # print each element without moving to the next line
        
original_array = [1,2,3,4,5,6,7,8,9]
reverse_array_extra_array(original_array)