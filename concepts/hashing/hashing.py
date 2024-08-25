def count_occurences(arr, queries):
    count_dict = {}
    
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    for query in queries:
        count = count_dict.get(query, 0)
        print(f"{query}: {count}")

arr = [1, 2, 1, 3, 2]
queries = [1, 3, 4, 2, 10]

string = "abcdabefc"
stringQueries = ['a','c','z']

count_occurences(arr, queries)
count_occurences(string, stringQueries)