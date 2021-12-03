def part1(lines):
    return sum(j > i for i, j in zip(lines, lines[1:]))
    
def part2(lines):
    lines = [i + j + k for i, j, k in zip(lines, lines[1:], lines[2:])]
    return part1(lines)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    lines = [int(i) for i in lines]
    print(part1(lines))
    print(part2(lines))
