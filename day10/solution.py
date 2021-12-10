p = {
    '}': '{',
    ']': '[',
    ')': '(',
    '>': '<'
}

pts = {
    '}': 1197,
    ']': 57,
    ')': 3,
    '>': 25137
}

inc = []

def illegal(l):            
    s = []
    for c in l:
        if c in '{[(<':
            s.append(c)
        else:
            if not s or s[-1] != p[c]:
                return pts[c]
            else:
                s.pop(-1)
    inc.append(s)
    return 0
    
def part1(lines):
    return sum(illegal(l) for l in lines)
    
pts2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}
    
def part2(lines):
    a = []
    for s in inc:
        s = s[::-1]
        sc = 0
        for p in s:
            sc *= 5
            sc += pts2[p]
        a.append(sc)
    a.sort()
    return a[len(a) // 2]

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    # lines = [int(i) for i in lines]
    print(part1(copy.deepcopy(lines)))
    print(part2(copy.deepcopy(lines)))
