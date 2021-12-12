from collections import defaultdict

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
            path.append(adj)
            total_paths += dfs(edges, path, allow_lower_dupe)
            path.pop(-1)
        elif allow_lower_dupe:
            path.append(adj)
            total_paths += dfs(edges, path, False)
            path.pop(-1)
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
