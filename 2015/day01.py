with open("day01.in") as f:
    s = f.read()

resulting_floor = 0
first_entered_basement = -1
for i, c in enumerate(s, 1):
    match c:
        case '(':
            resulting_floor += 1
        case ')':
            resulting_floor -= 1
    if first_entered_basement == -1 and resulting_floor == -1:
        first_entered_basement = i

# Day 1
print(resulting_floor)

# Day 2
print(first_entered_basement)
