import re
import math

with open('input.txt') as f:
	lines = f.read().splitlines()

instructions = lines[0]
network = {}
for line in lines[2:]:
	m = re.findall(r'[0-9A-Z]{3}', line)
	network[m[0]] = (m[1], m[2])

start_nodes = [node for node in network if node.endswith('A')]

all_steps = []
for node in start_nodes:
	steps = 0
	while True:
		for instruction in instructions:
			if instruction == 'L':
				node = network[node][0]
			elif instruction == 'R':
				node = network[node][1]

			steps += 1

		if node.endswith('Z'):
			break

	all_steps.append(steps)

print('All steps:', all_steps)
print('Least common multiple of all steps:', math.lcm(*all_steps))
