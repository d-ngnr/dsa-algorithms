# This solution will use an extra array to store the results
def reverse_array_extra_array(arr):
    """
    Reverses the given array using an extra array and prints the reversed array.

    Parameters:
        arr (list): The array to be reversed.

    Returns:
        None

    Time complexity: O(n), where n is the length of the input array.
    Space complexity: O(n), as an extra array is used to store the reversed elements.
    """
    
    print("Reversed array:", end=" ") # print without moving to the next line
    for i in reversed_array:
        print(i, end=" ")  # print each element without moving to the next line
        
original_array = [1,2,3,4,5,6,7,8,9]
reverse_array_extra_array(original_array)