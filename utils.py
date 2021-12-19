def read_file(file: str) -> list:
	lines = []
	with open(f"{file}.txt", 'r') as f:
		for line in f:
			lines.append(line)

	return lines

