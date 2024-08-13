with open("day03.in") as f:
    steps = f.read().strip()

def process_steps(steps):    
    x = y = 0
    houses = {(0,0)} # the first house always gets a present
    vectors = {
        '>': ( 1,  0),
        '<': (-1,  0),
        '^': ( 0,  1),
        'v': ( 0, -1),
    }
    
    for s in steps:
        dx, dy = vectors[s]
        x += dx
        y += dy
        houses.add((x, y))
    
    return houses

# Part 1
print(len(process_steps(steps)))

# Part 2
print(len(process_steps(steps[::2]).union(process_steps(steps[1::2]))))

