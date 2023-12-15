with open('input.txt') as f:
	lines = f.read().splitlines()

data = [[int(number) for number in line.split()] for line in lines]

total = 0
for numbers in data:
	while any(number != 0 for number in numbers):
		total += numbers[0]
		numbers = [numbers[i] - numbers[i+1] for i in range(len(numbers) - 1)]

print('Sum of extrapolated values:', total)
