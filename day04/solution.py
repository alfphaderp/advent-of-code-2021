def part1(nums, boards):
    for num in nums:
        for board in boards:
            mark_num(board, num)
        for board_idx in range(len(boards)):
            bingo_result = bingo(boards[board_idx])
            if bingo_result != 'NO BINGO':
                return bingo_result * num

def part2(nums, boards):
    bingoed = set()
    last_bingo_score = None
    for num in nums:
        for board in boards:
            mark_num(board, num)
        for board_idx in range(len(boards)):
            if board_idx not in bingoed:
                bingo_result = bingo(boards[board_idx])
                if bingo_result != 'NO BINGO':
                    bingoed.add(board_idx)
                    last_bingo_score = bingo_result * num
    return last_bingo_score

def mark_num(board, num):
    for row in board:
        for i in range(5):
            if row[i] == num:
                row[i] = 'X'

def bingo(board):
    for row in board:
        if all(num == 'X' for num in row):
            return score(board)
    for col in zip(*board):
        if all(num == 'X' for num in col):
            return score(board)
    return 'NO BINGO'

def score(board):
    return sum(board[i][j] for i in range(5) for j in range(5) if board[i][j] != 'X')

def group(lines):
    groups, group = [], []
    for line in lines:
        if line != "":
            group.append(line)
        else:
            groups.append(group)
            group = []
    groups.append(group)
    return groups

import copy

if __name__ == '__main__':
    file = 'input.txt'
    file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        
    nums = [int(i) for i in lines[0].split(',')]
    boards = [[[int(n) for n in r.split(' ') if n != ''] for r in b] for b in group(lines[2:])]
    
    print(part1(nums, copy.deepcopy(boards)))
    print(part2(nums, copy.deepcopy(boards)))
