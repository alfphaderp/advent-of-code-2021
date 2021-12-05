from collections import defaultdict

def part1(lines):
    # di = defaultdict(lambda: 0)
    # for l in lines:
    #     l = l.split(' ')
    #     a, b = l[0].split(',')
    #     c, d = l[-1].split(',')
    #     a, b, c, d = int(a), int(b), int(c), int(d)
    # 
    #     if a == c:
    #         b, d = min(b, d), max(b, d)
    #         for i in range(b, d + 1):
    #             di[a, i] += 1
    #     if b == d:
    #         a, c = min(a, c), max(a, c)
    #         for i in range(a, c + 1):
    #             di[i, b] += 1
    # return sum(1 for v in di.values() if v >= 2)
    pass
        
dit = None
    
def part2(lines):
    di = defaultdict(lambda: 0)
    for l in lines:
        l = l.split(' ')
        a, b = l[0].split(',')
        c, d = l[-1].split(',')
        a, b, c, d = int(a), int(b), int(c), int(d)
        
        if a == c:
            b, d = min(b, d), max(b, d)
            for i in range(b, d + 1):
                di[a, i] += 1
        elif b == d:
            a, c = min(a, c), max(a, c)
            for i in range(a, c + 1):
                di[i, b] += 1
        else:
            print(a, b, c, d)
            if a < c:
                dx = 1
            else:
                dx = -1
            if b < d:
                dy = 1
            else:
                dy = -1
                          
            for i in range(abs(a - c) + 1):
                # print(abs(a - b))
                di[a, b] += 1
                a += dx
                b += dy
                # print(a, b)
            
            # di[c, d] += 1
            # di[a, b] += 1
    global dit
    dit = di
    print_di(di)
    return sum(1 for v in di.values() if v >= 2)

def print_di(di):
    for j in range(10):
        for i in range(10):
            if (i, j) in di:
                print(di[i, j],end='')
            else:
                print('.',end='')
        print()

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    # lines = [int(i) for i in lines]
    print(part1(copy.deepcopy(lines)))
    print(part2(copy.deepcopy(lines)))
