from itertools import combinations

with open('input.txt') as f:
	universe = f.read().splitlines()

# Convert strings to lists
universe = [list(row) for row in universe]

# Calculate the number of rows and columns to add to the universe
rows = len(universe)
cols = len(universe[0])

# Find all rows and columns that are empty
empty_rows = [i for i, row in enumerate(universe) if all([c == '.' for c in row])]
empty_cols = [j for j in range(cols) if all([row[j] == '.' for row in universe])]

# Find all galaxies in the universe
galaxies = [(i, j) for i, row in enumerate(universe) for j, col in enumerate(row) if col == '#']

# Change the galxies coordinates to account for the empty rows and columns
galaxies = [(i + len([r for r in empty_rows if r < i]), j + len([c for c in empty_cols if c < j])) for i, j in galaxies]

# Iterate over all galaxy pairs and calculate the shortest paths between them
shortest_paths = [abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) for g1, g2 in combinations(galaxies, 2)]

print('Sum of shortest paths between all galaxies:', sum(shortest_paths))