def read_data(path):
    with open(path) as f:
        data = f.readlines()

    data = [x.strip() for x in data]
    data = [int(x) if x != '' else x for x in data]

    elfs = []
    prev_index = 0

    for i, x in enumerate(data):
        if x == '':
            elfs.append(data[prev_index:i])
            prev_index = i + 1

    if prev_index < len(data):
        elfs.append(data[prev_index:])

    return elfs


if __name__ == '__main__':
    elfs = read_data('input.txt')
    
    calories_sum = [sum(x) for x in elfs]
    
    calories_max = max(calories_sum)
    print(calories_max)
    
    calories_sum = list(sorted(calories_sum, reverse=True))
    
    calories_top_3 = sum(calories_sum[:3])
    print(calories_top_3)
