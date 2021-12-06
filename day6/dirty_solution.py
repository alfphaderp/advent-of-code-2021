def advance(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = 6
            nums.append(8)
        else:
            nums[i] -= 1

from functools import lru_cache

@lru_cache(None)
def forks(i, days):
    if days == 0:
        # print(i, end=' ')
        # if i == 0:
        #     print(8, end=' ')
        return 1 if i == 0 else 0
    if i == 0:
        return 1 + forks(6, days - 1) + forks(8, days - 1)
    return forks(i - 1, days - 1)

def part1(lines):
    nums = [int(i) for i in lines[0].split(',')]
    for _ in range(80):
        advance(nums)
    return len(nums)
    
def part2(lines):
    nums = [int(i) for i in lines[0].split(',')]
    # print(nums)
    nums = [1 + forks(n, 255) for n in nums]
    return sum(nums)

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    # lines = [int(i) for i in lines]
    print(part1(copy.deepcopy(lines)))
    print(part2(copy.deepcopy(lines)))
