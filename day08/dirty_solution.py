from collections import Counter

def part1(lines):
    total = 0
    for l in lines:
        left, right = l.split(' | ')
        right = right.split(' ')
        total += sum(1 for b in right if len(b) in [2, 4, 3, 7])
    return total

def part2(lines):
    total = 0
    for l in lines:
        inp, out = l.split(' | ')
        inp = inp.split(' ')
        out = out.split(' ')
        
        stn = {}
        nts = {}
        counts = Counter()
        for i in inp:
            counts += Counter(i)
            if len(i) == 2:
                stn[i] = 1
                nts[1] = i
            elif len(i) == 4:
                stn[i] = 4
                nts[4] = i
            elif len(i) == 3:
                stn[i] = 7
                nts[7] = i
            elif len(i) == 7:
                stn[i] = 8
                nts[8] = i
        bottom_right = [k for k, v in counts.items() if v == 9][0]
        bottom_left = [k for k, v in counts.items() if v == 4][0]
        top_left = [k for k, v in counts.items() if v == 6][0]
        top_right = (set(nts[1]) - set(bottom_right)).pop()
        top = (set(nts[7]) - set(nts[1])).pop()
        mid = (set(nts[4]) - set(nts[1]) - set([top_left])).pop()
        bot = (set([k for k, v in counts.items() if v == 7]) - set([mid])).pop()
        
        stn[[i for i in inp if len(i) == 6 and mid not in i][0]] = 0
        stn[[i for i in inp if len(i) == 5 and top_left not in i and bottom_right not in i][0]] = 2
        stn[[i for i in inp if len(i) == 5 and top_left not in i and bottom_left not in i][0]] = 3
        stn[[i for i in inp if len(i) == 5 and bottom_left not in i and top_right not in i][0]] = 5
        stn[[i for i in inp if len(i) == 6 and top_right not in i][0]] = 6
        stn[[i for i in inp if len(i) == 6 and bottom_left not in i][0]] = 9
        
        # print(stn)
        
        stn = {frozenset(s): v for s, v in stn.items()}
        
        asdf = []
        for o in out:
            if len(o) == 2:
                asdf.append(1)
            elif len(o) == 4:
                asdf.append(4)
            elif len(o) == 3:
                asdf.append(7)
            elif len(o) == 7:
                asdf.append(8)
            else:
                asdf.append(str(stn[frozenset(o)]))
        print(int(''.join(str(s) for s in asdf)))
        total += int(''.join(str(s) for s in asdf))
    return total

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    # lines = [int(i) for i in lines]
    print(part1(copy.deepcopy(lines)))
    print(part2(copy.deepcopy(lines)))
