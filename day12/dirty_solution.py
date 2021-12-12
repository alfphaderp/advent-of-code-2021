from collections import defaultdict, deque

def part1(lines):
    edges = defaultdict(list)
    for l in lines:
        a, b = l
        edges[a].append(b)
        edges[b].append(a)
    # 
    # print(edges)
    
    paths = []
    q = deque()
    q.append((False, ('start',)))
    while q:
        # print(q)
        asdf = q.pop()
        duped = asdf[0]
        curr = asdf[1]
        # print(asdf, duped, curr)
        if curr[-1] == 'end':
            paths.append(curr)
        else:
            for adj in edges[curr[-1]]:
                # print(curr, adj)
                if adj == 'start':
                    continue
                elif adj.islower():
                    if adj not in curr:
                        q.append((duped, (*curr, adj)))
                    elif not duped:
                        q.append((True, (*curr, adj)))
                elif adj.isupper() or adj not in curr:
                    q.append((duped, (*curr, adj)))
    # for p in paths:
    #     print(p)
    
    return len(paths)
    
def part2(lines):
    pass

def parse(lines):
    lines = [l.split('-') for l in lines]
    return lines

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    lines = parse(lines)
    print(part1(copy.deepcopy(lines)))
    print(part2(copy.deepcopy(lines)))
