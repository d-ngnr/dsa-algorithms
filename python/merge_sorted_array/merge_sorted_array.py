def merge_sorted_array(nums1, m, nums2, n):
    i,j = 0, 0
    nums3 = []
    
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i += 1
        else:
            nums3.append(nums2[j])
            j += 1
    
    if i < m:
        nums3.extend(nums1[i:])
        
    if j < n:
        nums3.extend(nums2[j:])
        
    return nums3
        
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge_sorted_array(nums1, m, nums2, n))
    