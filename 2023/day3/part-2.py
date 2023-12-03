import re

with open('input.txt', 'r') as file:
	lines = file.read().splitlines()

rows = len(lines)
cols = len(lines[0])

# Create a map to store the gear index and the numbers that are adjacent to it.
gear_map = {}

# Iterate over each line, and each number in each line.
for row in range(rows):
	line = lines[row]

	matches = re.finditer(r'\d+', line)

	# Iterate over each number in the line.
	for m in matches:
		number = int(m.group(0))
		gear_indecies = []

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

					# Check if the character is '*'
					if lines[i][j] == '*':
						gear_index = i * cols + j

						# Skip if the gear index is already in the map.
						if gear_index in gear_indecies:
							continue

						# Add the gear index to the map.
						if gear_index not in gear_map:
							gear_map[gear_index] = []

						# Add the number to the gear index.
						gear_map[gear_index].append(number)
						gear_indecies.append(gear_index)

# Create a variable to store the total sum.
total_sum = 0

# Iterate over the gear map.
for numbers in gear_map.values():
	# Check if the length of the numbers is 2 and add the power to the total sum.
	if len(numbers) == 2:
		total_sum += numbers[0] * numbers[1]

print(total_sum)
