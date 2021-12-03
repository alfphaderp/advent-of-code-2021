def part1(groups):
    pass
    
def part2(groups):
    pass

def group(lines):
    groups, group = [], []
    for line in lines:
        if line != "":
            group.extend(line.split(" "))
        else:
            groups.append(group)
            group = []
    groups.append(group)
    return groups

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        groups = group(f.read().splitlines())
    print(part1(groups))
    print(part2(groups))
