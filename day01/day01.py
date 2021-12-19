from ..utils import read_file

def part1(file: list) -> int:
	return len(file)

def part2(file: list) -> int:
	return len(file)

# Test File
test_file = read_file("day01_test")

assert part1(test_file) == 0
print(part1(test_file))

assert part2(test_file) == 0
print(part2(test_file))

# Actual File
actual_file = read_file("day01")

assert part1(actual_file) == 0
print(part1(actual_file))

assert part2(actual_file) == 0
print(part1(actual_file))
