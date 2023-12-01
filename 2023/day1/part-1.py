import re

with open('input.txt', 'r') as f:
	data = f.read().splitlines()


sum = 0
for line in data:
	digits = re.findall(r'\d', line)
	
	first_num = int(digits[0])
	last_num = int(digits[-1])

	num = first_num * 10 + last_num
	sum += num

print(sum)
