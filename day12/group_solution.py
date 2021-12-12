def part1(g):
    pass
    
def part2(g):
    pass

def group(lines):
    groups, group = [], []
    for line in lines:
        if line != "":
            group.append(line)
        else:
            groups.append(group)
            group = []
    groups.append(group)
    return groups

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        groups = group(f.read().splitlines())
    print(part1(copy.deepcopy(groups)))
    print(part2(copy.deepcopy(groups)))
