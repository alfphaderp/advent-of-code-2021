from collections import defaultdict

def part1(lines):
    return solve(lines, False)
    
def part2(lines):
    return solve(lines)

def solve(lines, diagonals=True):
    vents = defaultdict(lambda: 0)
    for line in lines:
        a, b, c, d = [*line[0], *line[1]]
        if not diagonals and a != c and b != d:
            continue
        dx = 1 if a < c else -1 if a > c else 0
        dy = 1 if b < d else -1 if b > d else 0
        for _ in range(max(abs(a - c), abs(b - d)) + 1):
            vents[a, b] += 1
            a += dx
            b += dy
    return sum(1 for v in vents.values() if v >= 2)

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    lines = [[[int(n) for n in xy.split(',')] for xy in l.split(' -> ')] for l in lines]
    print(part1(copy.deepcopy(lines)))
    print(part2(copy.deepcopy(lines)))
