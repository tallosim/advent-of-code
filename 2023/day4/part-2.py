import re

with open('input.txt', 'r') as file:
	lines = file.read().splitlines()

total_map = {}
winning_map = {}
for line in lines:
	m = re.match(r'Card +(\d+): ([\d ]*) \| ([\d ]*)', line)

	card_number = int(m.group(1))
	
	winning_numbers = [int(x) for x in re.findall(r'\d+', m.group(2))]
	my_numbers = [int(x) for x in re.findall(r'\d+', m.group(3))]

	intersection = list(set(winning_numbers).intersection(my_numbers))

	winning_map[card_number] = len(intersection)
	total_map[card_number] = 1

total_count = 0
for card_number, winning_count in sorted(winning_map.items(), key=lambda x: x[0]):
	for i in range(1, winning_count + 1):
		index = card_number + i
		if index not in total_map:
			continue

		total_map[index] += total_map[card_number]

	total_count += total_map[card_number]

print(total_count)