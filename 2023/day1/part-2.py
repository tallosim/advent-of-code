import re

with open('input.txt', 'r') as f:
	data = f.read().splitlines()

DIGIT_MAP = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9'
}

total_sum = 0
for line in data:
	digits = re.finditer(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
	digits = [d.group(1) for d in digits]

	good_digits = []
	for d in digits:
		if d in DIGIT_MAP:
			good_digits.append(DIGIT_MAP[d])
		else:
			good_digits.append(d)
	
	first_num = int(good_digits[0])
	last_num = int(good_digits[-1])

	num = first_num * 10 + last_num
	total_sum += num

print(total_sum)
