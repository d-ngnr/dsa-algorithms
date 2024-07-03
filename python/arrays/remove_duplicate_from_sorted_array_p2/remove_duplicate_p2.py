def remove_duplicates_p2(nums):
    i = 0
    for j in range(2, len(nums)):   # start from the second element
        if nums[j] != nums[i - 2]:  # if the current element is not equal to the previous two elements
            nums[i] = nums[j]       # swap the current element with the previous two elements
            i += 1                  # increment the index               
    return i                        # return the index

nums = [1,1,1,2,2,3,3,4,4,4,5]
new_size=remove_duplicates_p2(nums)
print(new_size)
print(nums[:new_size]) # Output: [1,2,3,4,5]