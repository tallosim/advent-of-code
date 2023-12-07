import re
from tqdm import tqdm

with open('input.txt', 'r') as file:
	lines = file.read().splitlines()

time = int(''.join(re.findall(r'\d+', lines[0])))
dist = int(''.join(re.findall(r'\d+', lines[1])))

record_beat_count = 0
for wait in tqdm(range(0, time + 1)):
	time_left = time - wait
	speed = wait * 1
	dist_traveled = speed * time_left

	if dist_traveled > dist:
		record_beat_count += 1

print(record_beat_count)
