import re

with open('input.txt', 'r') as file:
	lines = file.read().splitlines()

times = [int(x) for x in re.findall(r'\d+', lines[0])]
distances = [int(x) for x in re.findall(r'\d+', lines[1])]

combinations = []
for time, dist in zip(times, distances):
	record_beat_count = 0
	for wait in range(0, time+1):
		time_left = time - wait
		speed = wait * 1
		dist_traveled = speed * time_left

		if dist_traveled > dist:
			record_beat_count += 1

	combinations.append(record_beat_count)

if len(combinations) == 0:
	print('No combinations found')

else:
	result = 1
	for x in combinations:
		result *= x
	print(result)
