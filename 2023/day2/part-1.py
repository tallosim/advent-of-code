import re

with open('input.txt', 'r') as file:
	data = file.read().splitlines()

POSSIBLE_MAP = {
	'blue': 14,
	'green': 13,
	'red': 12
}

total_sum = 0
for line in data:
	possible = True
	game_number = int(re.search(r'Game (\d+):', line).group(1))

	drawes = line.split(': ')[1].split('; ')
	for draw in drawes:
		cubes = draw.split(', ')
		for cube in cubes:
			count, color = cube.split(' ')
			count = int(count)

			if POSSIBLE_MAP[color] < count:
				possible = False
				break

	if possible:
		total_sum += game_number

print(total_sum)