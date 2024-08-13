from collections import defaultdict

import re

pat = re.compile(r"([a-z\s]+[a-z]) (\d+),(\d+)\D+(\d+),(\d+)")

# Part 1

lights = set()
for line in open("day06.in"):
    result = pat.findall(line)[0]
    instruction, (x1, y1, x2, y2) = result[0], map(int, result[1:])
    match instruction:
        case 'turn on':
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights.add((x, y))
        case 'turn off':
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights.discard((x, y))
        case 'toggle':
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    try:
                        lights.remove((x, y))
                    except KeyError:
                        lights.add((x, y))
                        
print(len(lights))

# Part 2

lights = defaultdict(int)
for line in open("day06.in"):
    result = pat.findall(line)[0]
    instruction, (x1, y1, x2, y2) = result[0], map(int, result[1:])
    match instruction:
        case 'turn on':
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[(x, y)] += 1
        case 'turn off':
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[(x, y)] = max(0, lights[(x, y)] - 1)
        case 'toggle':
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[(x, y)] += 2
                    
print(sum(lights.values()))