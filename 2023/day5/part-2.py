import re

with open('input.txt') as f:
	data = f.read()

sections = data.split('\n\n')

seed_ranges = [int(x) for x in re.findall(r'\d+', sections[0])]
seed_ranges = [(start, start + length) for (start, length) in zip(seed_ranges[::2], seed_ranges[1::2])]

maps = []
for section in sections[1:]:
	lines = section.splitlines()
	maps.append([[int(x) for x in re.findall(r'\d+', l)] for l in lines[1:]])

locations = []
for seed_range in seed_ranges:
	stacks = [seed_range]
	new_stacks = []

	# Iterate over the maps
	for _map in maps:
		# Iterate over the current stack
		while len(stacks) > 0:
			# Pop the first range from the stack
			[start, end] = stacks.pop(0)

			for [dest_start, src_start, length] in _map:
				# If the source range is completely outside the current range, skip it
				if end < src_start or src_start + length <= start:
					continue

				# If the source range is completely inside the current range
				elif src_start <= start <= end < src_start + length:
					offset = start - src_start
					new_stacks.append((dest_start + offset, dest_start + offset + (end - start)))
					break

				# If the current range starts outside the source range, but ends inside it
				elif start < src_start <= end < src_start + length:
					offset = end - src_start
					new_stacks.append((dest_start, dest_start + offset))
					stacks.append((start, src_start - 1))
					break

				# If the current range starts inside the source range, but ends outside it
				elif src_start <= start < src_start + length <= end:
					offset = start - src_start
					new_stacks.append((dest_start + offset, dest_start + length - 1))
					stacks.append((src_start + length, end))
					break

				# If the current range starts and ends outside the source range
				elif start < src_start <= src_start + length <= end:
					new_stacks.append((dest_start, dest_start + length - 1))
					stacks.append((start, src_start - 1))
					stacks.append((src_start + length, end))
					break

			# If the current range is not affected by any of the mappings, add it to the new stack
			else:
				new_stacks.append((start, end))

		# Swap the stacks
		stacks = new_stacks
		new_stacks = []
	
	# Add only the start locations to the list of locations
	locations.extend([start for (start, _) in stacks])

print(min(locations))