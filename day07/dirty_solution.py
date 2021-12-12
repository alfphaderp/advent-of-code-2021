def tri(n):
    return n * (n + 1) // 2

def part1(lines):
    s, f = min(lines), max(lines)
    m = min(range(s, f + 1), key=lambda t: sum(abs(t - n) for n in lines))
    return sum(abs(m - n) for n in lines)
    
def part2(lines):
    s, f = min(lines), max(lines)
    m = min(range(s, f + 1), key=lambda t: sum(tri(abs(t - n)) for n in lines))
    return sum(tri(abs(m - n)) for n in lines)

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    lines = [int(i) for i in lines[0].split(',')]
    print(part1(copy.deepcopy(lines)))
    print(part2(copy.deepcopy(lines)))
