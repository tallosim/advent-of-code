import re

with open('input.txt') as f:
	lines = f.read().splitlines()

instructions = lines[0]
network = {}
for line in lines[2:]:
	m = re.findall(r'[A-Z]{3}', line)
	network[m[0]] = (m[1], m[2])

steps = 0
node = 'AAA'
while True:
	for instruction in instructions:
		if instruction == 'L':
			node = network[node][0]
		elif instruction == 'R':
			node = network[node][1]

		steps += 1

	if node == 'ZZZ':
		break

print('Steps:', steps)