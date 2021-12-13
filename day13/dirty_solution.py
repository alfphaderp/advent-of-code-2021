def part1(lines):
    pts, dirs = lines
    
    print(pts)
    
    xy, val = dirs[0]
    val = int(val)
    print(xy, val)
    
    new_pts = set()
    if xy == 'y':
        for p in pts:
            x, y = p
            if y < val:
                new_pts.add(p)
            else:
                new_pts.add((x, val - abs(val - y)))
    if xy == 'x':
        for p in pts:
            x, y = p
            if x < val:
                new_pts.add(p)
            else:
                new_pts.add((val - abs(val - x), y))
    pts = new_pts
    
    return len(new_pts)
    
def part2(lines):
    pts, dirs = lines
    
    for d in dirs:
        xy, val = d
        val = int(val)
        
        new_pts = set()
        if xy == 'y':
            for p in pts:
                x, y = p
                if y < val:
                    new_pts.add(p)
                else:
                    new_pts.add((x, val - abs(val - y)))
        if xy == 'x':
            for p in pts:
                x, y = p
                if x < val:
                    new_pts.add(p)
                else:
                    new_pts.add((val - abs(val - x), y))
        pts = new_pts
    
    print(pts)

def parse(lines):
    sp = lines.index('')
    pts = lines[:sp]
    pts = set([tuple(int(n) for n in p.split(',')) for p in pts])
    dirs = lines[sp + 1:]
    dirs = [d.split('g ')[1] for d in dirs]
    dirs = [d.split('=') for d in dirs]
    return [pts, dirs]

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
