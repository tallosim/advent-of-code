def read_data(path):
    with open(path) as f:
        data = f.readlines()
        
    data = [x.strip() for x in data]
    rounds = [x.split(' ') for x in data]
    
    return rounds


def calc_part_one_score(round):
    opponent = round[0]
    mine = round[1]
    
    XYZ_TO_ABC = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }
    mine = XYZ_TO_ABC[mine]
    
    base = ord(mine) - ord('A') + 1
    
    if  (opponent == 'B' and mine == 'A') or \
        (opponent == 'C' and mine == 'B') or \
        (opponent == 'A' and mine == 'C'):
        return base
    
    if opponent == mine:
        return base + 3
    
    return base + 6


def calc_part_two_score(round):
    opponent = round[0]
    result = round[1]
    
    if result == 'X':
        if opponent == 'A':
            return 0 + 3
        if opponent == 'B':
            return 0 + 1
        if opponent == 'C':
            return 0 + 2
    
    if result == 'Y':
        return 3 + ord(opponent) - ord('A') + 1
    
    if result == 'Z':
        if opponent == 'A':
            return 6 + 2
        if opponent == 'B':
            return 6 + 3
        if opponent == 'C':
            return 6 + 1


if __name__ == '__main__':
    rounds = read_data('input.txt')
    
    scores = [calc_part_one_score(x) for x in rounds]
    total_score = sum(scores)
    print(total_score)
    
    scores = [calc_part_two_score(x) for x in rounds]
    total_score = sum(scores)
    print(total_score)
