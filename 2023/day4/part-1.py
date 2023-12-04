import re

with open('input.txt', 'r') as file:
	lines = file.read().splitlines()

total_sum = 0
for line in lines:
	m = re.match(r'Card +(\d+): ([\d ]*) \| ([\d ]*)', line)
	
	winning_numbers = [int(x) for x in re.findall(r'\d+', m.group(2))]
	my_numbers = [int(x) for x in re.findall(r'\d+', m.group(3))]

	intersection = list(set(winning_numbers).intersection(my_numbers))

	if len(intersection) > 0:
		total_sum += 2 ** (len(intersection) - 1)

print(total_sum)
