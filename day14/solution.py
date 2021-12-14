from collections import Counter

def update(template, rules):
    final = []
    for a, b in zip(template, template[1:]):
        final.append(a)
        if a + b in rules:
            final.append(rules[a + b])
    final.append(template[-1])
    return ''.join(final)

def part1(lines):
    template, rules = lines
    
    for _ in range(10):
        template = update(template, rules)
    
    c = Counter(template)
    
    print(c)
    
    cv = c.values()
    
    return max(cv) - min(cv)

def update2(thing, rules):
    new_thing = Counter()
    for k, v in thing.items():
        if k in rules:
            f, l = k
            new_thing[f + rules[k]] += v
            new_thing[rules[k] + l] += v
        else:
            new_thing[k] += v
    return new_thing

def part2(lines):
    template, rules = lines
    thing = Counter(a + b for a, b in zip(template, template[1:]))
    
    for _ in range(40):
        thing = update2(thing, rules)
    
    totals = Counter()
    for k, v in thing.items():
        totals[k[0]] += v
    totals[template[-1]] += 1
    
    cv = totals.values()
    
    return max(cv) - min(cv)
    
    

def parse(lines):
    template = lines[0]
    rules = [l.split(' -> ') for l in lines[2:]]
    rules = {f: t for f, t in rules}
    return template, rules

import copy

if __name__ == '__main__':
    file = 'input.txt'
    # file = 'input_sample.txt'
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        f.close()
    lines = parse(lines)
    print(part1(copy.deepcopy(lines)))
    print(part2(copy.deepcopy(lines)))
