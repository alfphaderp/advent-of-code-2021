def part1(lines):
    pts, dirs = lines
    return len(flip(pts, *dirs[0]))
    
def part2(lines):
    pts, dirs = lines
    for d in dirs:
        pts = flip(pts, *d)
    return pts

def flip(pts, axis, value):
    if axis == 'x':
        return {(value - abs(value - p[0]), p[1]) for p in pts}
    else:
        return {(p[0], value - abs(value - p[1])) for p in pts}

def plot(pts):
    xs, ys = zip(*pts)
    for y in range(min(ys), max(ys) + 1):
        for x in range(min(xs), max(xs) + 1):
            print('██' if (x, y) in pts else '  ', end='')
        print()

def parse(lines):
    split_point = lines.index('')
    pts = set(tuple(int(n) for n in p.split(',')) for p in lines[:split_point])
    dirs = [d.split('g ')[1].split('=') for d in lines[split_point + 1:]]
    dirs = [(a, int(v)) for a, v in dirs]
    return pts, dirs

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        f.close()
    lines = parse(lines)
    print(part1(copy.deepcopy(lines)))
    plot(part2(copy.deepcopy(lines)))
