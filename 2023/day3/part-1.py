import re

with open('input.txt', 'r') as file:
	lines = file.read().splitlines()

rows = len(lines)
cols = len(lines[0])

total_sum = 0

# Iterate over each line, and each number in each line.
for row in range(rows):
	line = lines[row]

	matches = re.finditer(r'\d+', line)

	# Iterate over each number in the line.
	for m in matches:
		number = int(m.group(0))
		has_adjacent = False

		# Iterate over each character in the number.
		for col in range(m.start(), m.end()):

			# Iterate over the adjacent numbers.
			for i in range(row - 1, row + 2):
				for j in range(col - 1, col + 2):
					# Skip if the index is out of bounds.
					if i < 0 or i >= rows or j < 0 or j >= cols:
						continue

					# Skip if the index is the same as the current number.
					if i == row and j == col:
						continue

					# Check if the character is a special character.
					# Not a '.' or a digit.
					if lines[i][j] != '.' and not lines[i][j].isdigit():
						has_adjacent = True
						break

				# Break out of the loop if we found an adjacent number.
				if has_adjacent:
					break

			# Break out of the loop if we found an adjacent number.
			if has_adjacent:
				break

		# Add the number to the total sum if it has adjacent numbers.
		if has_adjacent:
			total_sum += number

print(total_sum)
