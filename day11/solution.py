from collections import defaultdict

def part1(octos):
    return sum(step(octos) for _ in range(100))
    
def part2(octos):
    i = 0
    while not all(val == 0 or val == float('-inf') for val in octos.values()):
        step(octos)
        i += 1
    return i
    
def step(octos):
    flash_queue, flashed = set(), set()
    
    for pos in octos.keys():
        octos[pos] += 1
        if octos[pos] > 9:
            flash_queue.add(pos)
    
    while flash_queue:
        pos = flash_queue.pop()
        flashed.add(pos)
        row, col = pos
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                octos[i, j] += 1
                if octos[i, j] > 9 and (i, j) not in flashed:
                    flash_queue.add((i, j))
    
    for pos in octos.keys():
        if octos[pos] > 9:
            octos[pos] = 0
    
    return len(flashed)

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    d = {(i, j): int(lines[i][j]) for j in range(len(lines)) for i in range(len(lines))}
    octos = defaultdict(lambda: float('-inf'), d)
    print(part1(copy.deepcopy(octos)))
    print(part2(copy.deepcopy(octos)))
