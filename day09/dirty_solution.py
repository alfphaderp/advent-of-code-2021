pts = set()

def part1(lines):
    lines = ['9' + l + '9' for l in lines]
    lines = ['9' * len(lines[0])] + lines
    lines.append('9' * len(lines[0]))
    total = 0
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[0]) - 1):
            if int(lines[i][j]) < int(lines[i - 1][j]) \
                    and int(lines[i][j]) < int(lines[i + 1][j]) \
                    and int(lines[i][j]) < int(lines[i][j - 1]) \
                    and int(lines[i][j]) < int(lines[i][j + 1]):
                total += int(lines[i][j]) + 1
                pts.add((i, j))
    return total

from collections import defaultdict
from random import randint

sizes = defaultdict(int)

def part2(lines):
    print(pts)
    lines = ['9' + l + '9' for l in lines]
    lines = ['9' * len(lines[0])] + lines
    lines.append('9' * len(lines[0]))
    lines = [[0 if n != '9' else 1 for n in l] for l in lines]
    
    l = []
    s = set()
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[0]) - 1):
            x = ff(lines, i, j, s)
            if x != 0:
                l.append(x)
    l.sort()
    print(l)
    a, b, c = l[-3:]
    print(a, b, c)
    return a * b * c

def ff(lines, i, j, s):
    if lines[i][j] == 0 and (i, j) not in s:
        s.add((i, j))
        return 1 + ff(lines, i + 1, j, s) + ff(lines, i - 1, j, s) + ff(lines, i, j + 1, s) + ff(lines, i, j - 1, s)
    return 0

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    # lines = [int(i) for i in lines]
    print(part1(copy.deepcopy(lines)))
    print(part2(copy.deepcopy(lines)))
