def product_of_array_except_self(arr):
    n = len(arr)
    answer = [1] * n
    
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= arr[i]
        
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= arr[i]
        
    return answer

# Example usage
arr = [1, 2, 3, 4]
print(product_of_array_except_self(arr))  # Output: [24, 12, 8, 6]