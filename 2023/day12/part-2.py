from functools import cache
from tqdm import tqdm

with open("input.txt") as f:
    lines = f.read().splitlines()

springs = [x.split(" ") for x in lines]
springs = [(x[0], [int(y) for y in x[1].split(",")]) for x in springs]

# We need to repeat the symbols and counts 5 times to get the correct answer
springs = [("?".join([symbols] * 5), counts * 5) for symbols, counts in springs]


# Cache is needed to avoid recalculating the same combinations over and over again
@cache
def count_permuations(symbols, counts, prev_group_size=0):
    # If no symbols left
    if symbols == "":
        # If there only one group left and it's the same size as the previous group it's valid
        if len(counts) == 1 and counts[0] == prev_group_size:
            return 1
        
        # If there are no groups left and the previous group size is 0 it's valid
        if len(counts) == 0 and prev_group_size == 0:
            return 1
        
        # Otherwise, this is not a valid combination
        return 0
    
    # If there are no groups left
    if len(counts) == 0:
        # If there are symobls left with "#" in them
        # or if the previous group size is greater than 0
        if "#" in symbols or prev_group_size > 0:
            return 0
        
        # Otherwise, this is a valid combination
        return 1
    
    result = 0

    symbol = symbols[0]
    possibilities = [".", "#"] if symbol == "?" else [symbol]
    
    for possibility in possibilities:
        # If the possibility is a "#", we're in a group
        if possibility == "#":
            result += count_permuations(symbols[1:], counts, prev_group_size + 1)

        # If the possibility is a ".", we're not in a group
        else:
            # If the previous group size is greater than 0, so we were in a group
            if prev_group_size > 0:
                # If the previous group size is the same as the first count
                if prev_group_size == counts[0]:
                    # Remove the first count
                    result += count_permuations(symbols[1:], counts[1:], 0)
                
                # Otherwise, this is not a valid combination
                else:
                    continue

            # If the previous group size is 0, so we were not in a group
            else:
                result += count_permuations(symbols[1:], counts, 0)

    return result

# Lists are not hashable, so we need to convert them to tuples
springs = [(symbols, tuple(counts)) for symbols, counts in springs]

results = [count_permuations(symbols, counts) for symbols, counts in tqdm(springs)]

print("Total:", sum(results))
