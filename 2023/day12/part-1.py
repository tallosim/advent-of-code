from itertools import product
from tqdm import tqdm

with open("input.txt") as f:
    lines = f.read().splitlines()

springs = [x.split(" ") for x in lines]
springs = [(x[0], [int(y) for y in x[1].split(",")]) for x in springs]

total = 0
for symbols, counts in tqdm(springs):
    possibleities = [[".", "#"] if s == "?" else s for s in symbols]
    combinations = ["".join(c) for c in list(product(*possibleities))]

    for combination in combinations:
        damaged_springs = [c for c in combination.split(".") if c != ""]
        lengths = [len(s) for s in damaged_springs]

        if lengths == counts:
            total += 1

print("Total:", total)
