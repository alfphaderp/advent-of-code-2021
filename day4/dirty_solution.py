def score(b, board):
    # print(b, board)
    total = 0
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] != 'X':
                total += board[i][j]
    return total

def bingo(b, boards):
    for r in b:
        if all(c == 'X' for c in r):
            return score(b, boards)
    for c in zip(*b):
        if all(r == 'X' for r in c):
            return score(b, boards)
    return False

def part1(nums, boards):    
    boards = [[int(n) for n in b if n.isnumeric()] for b in boards]
    boards = [[b[i * 5:i * 5 + 5] for i in range(5)] for b in boards]
    
    boards2 = [[list(l) for l in b] for b in boards]
    
    print(nums)
    for b in boards:
        print(b)
    bingoed = set()
    
    for n in nums:
        for b in boards:
            for r in b:
                for i in range(5):
                    if r[i] == n:
                        r[i] = 'X'
        for i in range(len(boards)):
            if bingo(boards[i], boards2[i]):
                if i not in bingoed:
                    bingoed.add(i)
                    print(bingo(boards[i], boards2[i]) * n)

def part2(nums, boards):
    pass

def group(lines):
    groups, group = [], []
    for line in lines:
        if line != "":
            group.extend(line.split(" "))
        else:
            groups.append(group)
            group = []
    groups.append(group)
    return groups

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        
    nums = [int(i) for i in lines[0].split(',')]
    
    boards = group(lines[2:])
    
    print(part1(nums, boards))
    print(part2(nums, boards))
