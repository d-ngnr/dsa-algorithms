def count_frequency(arr):
    frequency_dict = {}
    
    for element in arr:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    
    for element in frequency_dict:
        count = frequency_dict.get(element, 0)
        print(f"{element}: {count}")
        
arr = [10,5,10,15,10,5]
count_frequency(arr)