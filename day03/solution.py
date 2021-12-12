def part1(lines):    
    gamma = ''.join('1' if col.count('1') > col.count('0') else '0' for col in zip(*lines))
    epsilon = ''.join('0' if bit == '1' else '1' for bit in gamma)
    return int(gamma, 2) * int(epsilon, 2)

def part2(lines):
    o2_choices, co2_choices = [int(l, 2) for l in lines], [int(l, 2) for l in lines]
    mask = 1 << len(lines[0]) - 1
    while mask > 0:
        if len(o2_choices) > 1:
            set_choices = [c for c in o2_choices if c & mask]
            unset_choices = [c for c in o2_choices if not c & mask]
            o2_choices = set_choices if len(set_choices) >= len(unset_choices) else unset_choices
        if len(co2_choices) > 1:
            set_choices = [c for c in co2_choices if c & mask]
            unset_choices = [c for c in co2_choices if not c & mask]
            co2_choices = unset_choices if len(set_choices) >= len(unset_choices) else set_choices
        mask >>= 1
    return int(o2_choices[0]) * int(co2_choices[0])

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
