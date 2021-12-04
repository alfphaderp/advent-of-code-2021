def part1(lines):
    pass
    
def part2(lines):
    pass

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    # lines = [int(i) for i in lines]
    print(part1(copy.deepcopy(lines)))
    print(part2(copy.deepcopy(lines)))
