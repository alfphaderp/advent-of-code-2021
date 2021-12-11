def flash(lines, i, j):
    pass

def adv(lines, xx):
    if all(all(n == 0 or n == float('-inf') for n in l) for l in lines):
        print(xx)
    
    # print(xx)
    # print(lines)
    
    updated = set()
    to_update = set()
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[0]) - 1):
            lines[i][j] += 1
            if lines[i][j] > 9:
                to_update.add((i, j))
    
    while to_update:
        curr = to_update.pop()
        updated.add(curr)
        y, x = curr
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                lines[i][j] += 1
                if lines[i][j] > 9 and (i, j) not in updated:
                    to_update.add((i, j))
    
    flashes = sum(sum(1 for n in l if n > 9) for l in lines)
    for l in lines:
        for i, n in enumerate(l):
            if n > 9:
                l[i] = 0
    
    return flashes

def part1(lines):
    lines = [list(int(n)for n in l) for l in lines]
    lines.append([float('-inf')] * len(lines))
    lines = [[float('-inf')] * len(lines)] + lines
    lines = [[float('-inf')] + l + [float('-inf')] for l in lines]
    
    total = 0
    for _ in range(999):
        total += adv(lines, _)
    
    return total
        
    
def part2(lines):
    pass
    # lines = [list(int(n)for n in l) for l in lines]
    # lines.append([float('-inf')] * len(lines))
    # lines = [[float('-inf')] * len(lines)] + lines
    # lines = [[float('-inf')] + l + [float('-inf')] for l in lines]
    # 
    # total = 0
    # for i in range(200):
    #     total += adv(lines)
    #     print(lines)

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    # lines = [int(i) for i in lines]
    print(part1(copy.deepcopy(lines)))
    print(part2(copy.deepcopy(lines)))
