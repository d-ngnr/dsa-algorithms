import sys
from typing import List

def parse_input(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return file.readlines()

def solve_part1(data: List[str]) -> int:
    left = []
    right = []
    
    for line in data:
        line = line.strip()
        left.append(line.split('   ')[0])
        right.append(line.split('   ')[1])
    
    left = sorted(left)
    right = sorted(right)
    
    differences = []
    for i in range(len(left)):
        differences.append(abs(int(left[i]) - int(right[i])))
    return sum(differences)

def solve_part2(data: List[str]) -> int:
    left = []
    right = []
    
    for line in data:
        line = line.strip()
        left.append(line.split('   ')[0])
        right.append(line.split('   ')[1])
    
    return sum([int(element) * right.count(element) for element in left])

def run_tests():
    test_data = [
        "1   2",
        "2   1",
        "3   3",
        "2   2",
    ]
    assert solve_part1(test_data) == 0, "Part 1 test failed"
    assert solve_part2(test_data) == 12, "Part 2 test failed"
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
    
    input_data = parse_input('day1.txt')
    print(f"Part 1 solution: {solve_part1(input_data)}")
    print(f"Part 2 solution: {solve_part2(input_data)}")