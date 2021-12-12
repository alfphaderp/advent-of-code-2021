def part1(lines):
    horiz_pos = depth = 0
    for l in lines:
        direction, x = l.split(' ')
        x = int(x)
        if direction == 'forward':
            horiz_pos += x
        elif direction == 'down':
            depth += x
        else:
            depth -= x
    return horiz_pos * depth

def part2(lines):
    horiz_pos = depth = aim = 0
    for l in lines:
        direction, x = l.split(' ')
        x = int(x)
        if direction == 'forward':
            horiz_pos += x
            depth += aim * x
        elif direction == 'down':
            aim += x
        else:
            aim -= x
    return horiz_pos * depth

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
