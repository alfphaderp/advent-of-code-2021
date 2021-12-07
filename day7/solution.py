def part1(positions):
    fuel_func = lambda target: sum(abs(target - p) for p in positions)
    target_pos = find_optimal_target_binary_search(positions, fuel_func)
    return fuel_func(target_pos)
    
def part2(positions):
    fuel_func = lambda target: sum(triangular(abs(target - p)) for p in positions)
    target_pos = find_optimal_target_binary_search(positions, fuel_func)
    return fuel_func(target_pos)

def triangular(n):
    return n * (n + 1) // 2

def find_optimal_target_brute_force(positions, fuel_func):
    return min(range(min(positions), max(positions)), key=fuel_func)

def find_optimal_target_binary_search(positions, fuel_func):
    lower_bound, upper_bound = min(positions), max(positions)
    best_target, best_fuel = float('inf'), float('inf')
    while lower_bound < upper_bound:
        midpoint = (lower_bound + upper_bound) // 2
        midpoint_fuel = fuel_func(midpoint)
        if midpoint_fuel < best_fuel:
            best_target = midpoint
            best_fuel = midpoint_fuel
        gradient = fuel_func(midpoint + 1) - midpoint_fuel
        if gradient > 0:
            upper_bound = midpoint - 1
        else:
            lower_bound = midpoint + 1
    return best_target

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    nums = [int(i) for i in lines[0].split(',')]
    print(part1(copy.deepcopy(nums)))
    print(part2(copy.deepcopy(nums)))
