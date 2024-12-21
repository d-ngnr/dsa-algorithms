import sys
import re
from typing import List

def parse_input(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return file.readlines()
    
def solve_part1(data: List[str]) -> int:
    sum = 0
    for line in data:
        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)

        for match in matches:
            nums = re.findall(r"\d{1,3}", match)
            sum += int(nums[0]) * int(nums[1])

    return sum

def solve_part2(data: List[str]) -> int:
    total = 0
    enable = True
    for line in data:
        pattern = re.compile(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)')
        instructions = re.findall(pattern, line)

        for i in instructions:
            if i == 'do()':
                enable = True
            elif i == 'don\'t()':
                enable = False
            else:
                if enable:
                    n1, n2 = re.findall(r'\d+', i)
                    total += int(n1) * int(n2)
                    
    return total
        
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
    skip = False
    input_data = parse_input('day3.txt')
    print(f"Part 1 solution: {solve_part1(input_data)}")
    print(f"Part 2 solution: {solve_part2(input_data)}")