def productExceptSelf(nums):
    n = len(nums)                                   # get length of array
    answer = [1] * n                                # initialize answer array
    
    left_product = 1                                # initialize going to the left product
    for i in range(n - 1, -1, -1):                  # iterate from right to left
        answer[i] *= left_product                   # update answer array       
        left_product *= nums[i]                     # update left product         
        
    right_product = 1                               # initialize going to the right product
    for i in range(n):                              # iterate from left to right              
        answer[i] *= right_product                  # update answer array    
        right_product *= nums[i]                    # update right product      
        
    return answer                                   # return answer array                    

nums = [1, 2, 3, 4]
print(productExceptSelf(nums))          # [24,12,8,6]

nums = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums))          # [0,0,9,0,0]