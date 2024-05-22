def get_min_max_value(arr):
    # print(f"{min(arr)} {max(arr)}")
    return [min(arr), max(arr)]

original_array = {3, 2, 1, 56, 10000, 167}
[print(a, end=" ") for a in get_min_max_value(original_array)]
print()