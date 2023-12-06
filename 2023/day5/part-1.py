import re

with open('input.txt') as f:
	data = f.read()

sections = data.split('\n\n')

seeds = [int(x) for x in re.findall(r'\d+', sections[0])]
maps = []

for section in sections[1:]:
	lines = section.splitlines()
	maps.append([[int(x) for x in re.findall(r'\d+', l)] for l in lines[1:]])
	
locations = []
for seed in seeds:
	x = seed
	for _map in maps:
		for [dest_start, src_start, length] in _map:
			if x >= src_start and x < src_start + length:
				x = dest_start + (x - src_start)
				break

	locations.append(x)
	print(seed, '->', x)

print(min(locations))