from collections import defaultdict
import heapq

def part1(lines):
    dist = {}
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            dist[i, j] = float('inf')
    dist[0, 0] = 0
    q = set((i, j) for i in range(len(lines)) for j in range(len(lines[0])))
    
    while q:
        curr = min(q, key=lambda p: dist[p])
        q.remove(curr)
        i, j = curr
        for i2, j2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if i2 == len(lines) or j2 == len(lines[0]) or i2 < 0 or j2 < 0:
                continue
            alt = dist[curr] + lines[i2][j2]
            if alt < dist[i2, j2]:
                dist[i2, j2] = alt
    
    return dist[len(lines) - 1, len(lines[0]) - 1]
    
from functools import lru_cache
import heapq
    
def part2(lines):
    r, c = len(lines), len(lines[0])
    lines = [l * 5 for l in lines]
    for _ in range(4):
        for i in range(r):
            lines.append(list(lines[i]))
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            lines[i][j] = lines[i][j] + (i // r) + (j // c)
            while lines[i][j] > 9:
                lines[i][j] -= 9
    
    dist = {}
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            dist[i, j] = float('inf')
    dist[0, 0] = 0
    q = [(float('inf'), i, j) for i in range(len(lines)) for j in range(len(lines[0]))]
    q[0] = (0, 0, 0)
    heapq.heapify(q)
    visited = set()
    
    while q:
        p, i, j = heapq.heappop(q)
        if dist[i, j] != p or (i, j) in visited:
            continue
        visited.add((i, j))
        for i2, j2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if i2 == len(lines) or j2 == len(lines[0]) or i2 < 0 or j2 < 0:
                continue
            alt = dist[i, j] + lines[i2][j2]
            if alt < dist[i2, j2]:
                dist[i2, j2] = alt
                heapq.heappush(q, (alt, i2, j2))
    
    return dist[len(lines) - 1, len(lines[0]) - 1]

def parse(lines):
    lines = [[int(i) for i in l] for l in lines]
    return lines

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        f.close()
    lines = parse(lines)
    print(part1(copy.deepcopy(lines)))
    print(part2(copy.deepcopy(lines)))
