from collections import defaultdict, deque

def part1(edges):
    return dfs(edges, allow_lower_dupe=False)

def part2(edges):
    return dfs(edges, allow_lower_dupe=True)

def dfs(edges, path=['start'], allow_lower_dupe=False):
    total_paths = 0
    for adj in edges[path[-1]]:
        if adj == 'start':
            continue
        elif adj == 'end':
            total_paths += 1
        elif adj.isupper() or adj not in path:
            total_paths += dfs(edges, path + [adj], allow_lower_dupe)
        elif allow_lower_dupe:
            total_paths += dfs(edges, path + [adj], False)
    return total_paths

def bfs(edges, allow_lower_dupe=False):
    total_paths = 0
    q = deque([[['start'], allow_lower_dupe]])
    while q:
        path, allow_lower_dupe = q.popleft()
        for adj in edges[path[-1]]:
            if adj == 'start':
                continue
            elif adj == 'end':
                total_paths += 1
            elif adj.isupper() or adj not in path:
                q.append([path + [adj], allow_lower_dupe])
            elif allow_lower_dupe:
                q.append([path + [adj], False])
    return total_paths

def parse(lines):
    edges = defaultdict(list)
    for line in lines:
        vertex_a, vertex_b = line.split('-')
        edges[vertex_a].append(vertex_b)
        edges[vertex_b].append(vertex_a)
    return edges

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    edges = parse(lines)
    print(part1(copy.deepcopy(edges)))
    print(part2(copy.deepcopy(edges)))
