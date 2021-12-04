def most_frequent_bit(num):
    zeroes, ones = num.count('0'), num.count('1')
    if zeroes == ones:
        return None
    return '0' if zeroes > ones else '1'

def part1(lines):    
    gamma = ''.join('1' if col.count('1') > col.count('0') else '0' for col in zip(*lines))
    epsilon = ''.join('0' if bit == '1' else '1' for bit in gamma)
    return int(gamma, 2) * int(epsilon, 2)

def part2(lines):
    o2_candidates = lines
    for i in range(len(lines[0])):
        frequent_bit = most_frequent_bit([l[i] for l in o2_candidates])
        keep_bit = '0' if frequent_bit == '0' else '1'
        o2_candidates = [c for c in o2_candidates if c[i] == keep_bit]
    o2_rating = int(''.join(o2_candidates[0]), 2)
    
    co2_candidates = lines
    for i in range(len(lines[0])):
        if len(co2_candidates) == 1:
            co2_rating = int(''.join(co2_candidates[0]), 2)
            break
        frequent_bit = most_frequent_bit([l[i] for l in co2_candidates])
        keep_bit = '1' if frequent_bit == '0' else '0'
        co2_candidates = [c for c in co2_candidates if c[i] == keep_bit]
    if len(co2_candidates) == 1:
        co2_rating = int(''.join(co2_candidates[0]), 2)
    
    return o2_rating * co2_rating

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    print(part1(lines))
    print(part2(lines))
