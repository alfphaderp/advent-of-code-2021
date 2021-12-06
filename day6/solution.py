from collections import deque
from functools import lru_cache

def part1(nums):
    return solve_queue(nums, 80)
    
def part2(nums):
    return solve_queue(nums, 256)

def solve_queue(nums, days):
    timers = deque([nums.count(i) for i in range(9)])
    for _ in range(days):
        timers.append(timers.popleft())
        timers[6] += timers[-1]
    return sum(timers)

def solve_dp(nums, days):
    @lru_cache(None)
    def count_forks(timer, days):
        if days == 0:
            return 1 if i == 0 else 0
        if i == 0:
            return 1 + forks(6, days - 1) + forks(8, days - 1)
        return forks(i - 1, days - 1)
    return sum(1 + forks(n, days - 1) for n in nums)

def solve_simulation(nums, days):
    for _ in range(days):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = 6
                nums.append(8)
            else:
                nums[i] -= 1
    return len(nums)

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    nums = [int(i) for i in lines[0].split(',')]
    print(part1(copy.deepcopy(nums)))
    print(part2(copy.deepcopy(nums)))
