from ..utils import read_file

def part1(file: list) -> int:
	return len(file)

def part2(file: list) -> int:
	return len(file)

test_file = read_file("day02_test")
assert part1(test_file) == 0
assert part2(test_file) == 0

actual_file = read_file("day02")
assert part1(actual_file) == 0
assert part2(actual_file) == 0
