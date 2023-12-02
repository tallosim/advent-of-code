with open('input.txt', 'r') as file:
	data = file.read().splitlines()

total_sum = 0
for line in data:
	cube_dict = {}

	drawes = line.split(': ')[1].split('; ')
	for draw in drawes:
		cubes = draw.split(', ')
		for cube in cubes:
			count, color = cube.split(' ')
			count = int(count)

			if color in cube_dict:
				if cube_dict[color] < count:
					cube_dict[color] = count
			else:
				cube_dict[color] = count

	power = 1
	for count in cube_dict.values():
		power *= count

	total_sum += power

print(total_sum)