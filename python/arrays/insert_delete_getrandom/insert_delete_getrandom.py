import random

class RandomizedSet:
    def __init__(self):
        self.list = []                      # list of random
        self.dict = {}                      # dict of random
    
    def insert(self, val):
        if val in self.dict:                # if val is already in the list
            return False                    # return False
        self.dict[val] = len(self.list)     # add val to the dictionary
        self.list.append(val)               # add val to the list
        return True                         # return True
    
    def remove(self, val):
        if val not in self.dict:             # if val is not in the list
            return False                     # return False
        last_element = self.list[-1]         # get the last element
        index = self.dict[val]               # get the index of the last element
        self.list[index] = last_element      # swap the last element with the current element
        self.dict[last_element] = index      # swap the index with the last element
        self.list.pop()                      # remove the last element
        del self.dict[val]                   # remove the val from the dictionary
        return True                          # return True
    
    def getRandom(self):
        return random.choice(self.list)      # get a random element from the list

# Example usage
randomSet = RandomizedSet()
print(randomSet.insert(1))                   # Output: True
print(randomSet.insert(2))                   # Output: True
print(randomSet.remove(2))                   # Output: True
print(randomSet.insert(2))                   # Output: False
print(randomSet.getRandom())                 # Output: 1 or 2