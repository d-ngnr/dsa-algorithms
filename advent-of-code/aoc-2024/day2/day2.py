import sys
from typing import List

def parse_input(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return file.readlines()
 
def isSafe(data: List[str]) -> bool:
    differences = []
    slider = 0
    if isAscending(data):
        while slider < len(data) -1:
            diff = int(data[slider + 1]) - int(data[slider])
            differences.append(diff)
            slider += 1
        for diff in differences:
            if diff not in [1, 2, 3]:
                return False
        return True
    if isDescending(data):
        while slider < len(data) -1:
            diff = int(data[slider]) - int(data[slider + 1])
            differences.append(diff)
            slider += 1
        for diff in differences:
            if diff not in [1, 2, 3]:
                return False
        return True

def isAscending(data: List[str]) -> bool:
    for i in range(len(data) - 1):
        if int(data[i]) > int(data[i + 1]):
            return False
    return True
def isDescending(data: List[str]) -> bool:
    for i in range(len(data) - 1):
        if int(data[i]) < int(data[i + 1]):
            return False
    return True

def solve_part1(data: List[str]) -> int:
    currentLine = []
    safeCount = 0
    
    for line in data:
        line = line.strip()
        currentLine = line.split()
        isSafeList = isSafe(currentLine)
        
        if isSafeList:
            safeCount = safeCount + 1
    
    return safeCount

def solve_part2(data: List[str]) -> int:
    lines = [line.split() for line in data]
    lines = [[int(n) for n in line] for line in lines]
    return count_safe_new(lines)

def count_safe_new(lines) -> int:
	num = 0
	for line in lines:
		if(is_safe(line) or can_be_safe(line)):
			num += 1
	return num

def is_safe(line) -> bool:
	all_inc = True
	all_dec = True
	for i in range(1, len(line)):
		if(line[i] - line[i-1] < 1 or line[i] - line[i-1] > 3):
			all_inc = False
		if(line[i] - line[i-1] < -3 or line[i] - line[i-1] > -1):
			all_dec = False

	return all_inc or all_dec

def can_be_safe(lines) -> bool:
	for i in range(len(lines)):
		new_rep = lines[:i] + lines[i+1:]
		if(is_safe(new_rep)):
			return True
	return False

def run_tests():
    test_data = [
        "28 25 25 22 19 16",
        "28 29 29 30 33 36"
    ]
    assert solve_part1(test_data) == 0, "Part 1 test failed"
    assert solve_part2(test_data) == 12, "Part 2 test failed"
    print("All tests passed!")

if __name__ == "__main__":
    #run_tests()
    
    input_data = parse_input('day2.txt')
    print(f"Part 1 solution: {solve_part1(input_data)}")
    print(f"Part 2 solution: {solve_part2(input_data)}")