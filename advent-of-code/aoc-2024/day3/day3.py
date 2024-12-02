import sys
from typing import List

def parse_input(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return file.readlines()
    
def solve_part1(data: List[str]) -> int:
    pass

def solve_part2(data: List[str]) -> int:
    pass
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
    
    input_data = parse_input('day3.txt')
    print(f"Part 1 solution: {solve_part1(input_data)}")
    print(f"Part 2 solution: {solve_part2(input_data)}")