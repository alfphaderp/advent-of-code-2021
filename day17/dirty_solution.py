def part1(lines):
    xi, xf, yi, yf = lines
    best_y = 0    
    for dx in range(-70, 70):
        for dy in range(10000):
            max_y = is_simulate_good(dx, dy, xi, xf, yi, yf)
            if max_y != -1:
                best_y = max(best_y, max_y)
    return best_y
            
def is_simulate_good(dx, dy, xi, xf, yi, yf):
    x, y = 0, 0
    max_y = 0
    good = False
    for _ in range(1000):
        if in_range(x, y, xi, xf, yi, yf):
            good = True
        x += dx
        y += dy
        max_y = max(max_y, y)
        if dx > 0:
            dx -= 1
        if dx < 0:
            dx += 1
        dy -= 1
    return max_y if good else -1
    
def in_range(x, y, xi, xf, yi, yf):
    return xi <= x <= xf and yi <= y <= yf

def part2(lines):
    xi, xf, yi, yf = lines
    total = 0
    for dx in range(80):
        for dy in range(-200, 10000):
            max_y = is_simulate_good(dx, dy, xi, xf, yi, yf)
            if max_y != -1:
                # print(dx, dy)
                total += 1
    return total

def parse(lines):
    xs, ys = lines[0].split(', ')
    xi, xf = [int(i) for i in xs.split('=')[1].split('..')]
    yi, yf = [int(i) for i in ys.split('=')[1].split('..')]
    return xi, xf, yi, yf

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
