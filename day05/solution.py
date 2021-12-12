from collections import defaultdict

def part1(lines):
    return solve(lines, False)
    
def part2(lines):
    return solve(lines)

def solve(lines, diagonals=True):
    vents = defaultdict(lambda: 0)
    for line in lines:
        start_x, start_y, end_x, end_y = *line[0], *line[1]
        if not diagonals and start_x != end_x and start_y != end_y:
            continue
        dx = 1 if start_x < end_x else -1 if start_x > end_x else 0
        dy = 1 if start_y < end_y else -1 if start_y > end_y else 0
        x, y = start_x, start_y
        for _ in range(max(abs(start_x - end_x), abs(start_y - end_y)) + 1):
            vents[x, y] += 1
            x += dx
            y += dy
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
