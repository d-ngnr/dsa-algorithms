from collections import Counter

def count_occurrences(arr, queries):
    count_dict = Counter(arr)
    
    for query in queries:
        print(f"{query}: {count_dict[query]}")

arr = [1,2,1,3,2]
queries = [1,3,4,2,10]

count_occurrences(arr, queries)