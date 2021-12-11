def part1(lines):
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    total = 0
    for line in lines:
        state, symbol = verify(line)
        if state == 'CORRUPTED':
            total += points[symbol]
    return total

def part2(lines):
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = []
    for line in lines:
        state, stack = verify(line)
        if state == 'INCOMPLETE':
            score = 0
            for symbol in stack[::-1]:
                score *= 5
                score += points[symbol]
            scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]

def verify(line):
    opening = {'}': '{', ']': '[', ')': '(', '>': '<'}
    stack = []
    for symbol in line:
        if symbol in '{[(<':
            stack.append(symbol)
        else:
            if not stack or stack[-1] != opening[symbol]:
                return 'CORRUPTED', symbol
            else:
                stack.pop(-1)
    return 'INCOMPLETE', stack

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    print(part1(copy.deepcopy(lines)))
    print(part2(copy.deepcopy(lines)))
