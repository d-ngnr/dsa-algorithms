def get_frequency(arr):
    frequency_dict = {}
    
    for element in arr:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
        
    max_count = max(frequency_dict.values())
    min_count = min(frequency_dict.values())
    
    min_num = [num for num, count in frequency_dict.items() if count == min_count]
    max_num = [num for num, count in frequency_dict.items() if count == max_count]
    
    print("Numbers with minimum occurrences:", ' '.join(f"{num}: {min_count}" for num in min_num))
    print("Numbers with maximum occurrences:", ' '.join(f"{num}: {max_count}" for num in max_num))

arr = [10, 5, 10, 15, 10, 5]
get_frequency(arr)