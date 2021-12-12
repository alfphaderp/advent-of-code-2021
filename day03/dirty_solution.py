def part1(l):
    n = len(l)
    ones = [0 for _ in range(len(l[0]))]
    for a in l:
        for i, b in enumerate(a):
            # print(i)
            ones[i] += int(b)
    ones = ['1' if o > n // 2 else '0' for o in ones]
    g = int(''.join(ones), 2)
    ones = ['0' if o == '1' else '1' for o in ones]
    e = int(''.join(ones), 2)
    return g * e
    
def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
    
def part2(l):
    b = list(l)
    a = []
    for i in range(len(l[0])):
        print(l)
        ones = zeros = 0
        for n in l:
            if n[i] == '1':
                ones += 1
            else:
                zeros += 1
        
        target = '1' if ones >= zeros else '0'
        a.append(target)
        l = [n for n in l if n[i] == target]
    e = int(''.join(a), 2)
    
    print(a)
    l = b
    a = []
    for i in range(len(l[0])):
        
        print(l)
        ones = zeros = 0
        for n in l:
            if n[i] == '1':
                ones += 1
            else:
                zeros += 1
        
        if len(l) == 1:
            target = n[i]
        else:
            target = '0' if ones >= zeros else '1'
        a.append(target)
        l = [n for n in l if n[i] == target]
    g = int(''.join(a), 2)
        
    print(g * e)

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    # lines = [int(i) for i in lines]
    print(part1(lines))
    print(part2(lines))
