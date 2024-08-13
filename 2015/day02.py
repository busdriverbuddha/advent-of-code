wrapping_paper = 0
ribbon = 0

for line in open("day02.in"):
    d1, d2, d3 = sorted(map(int, line.split("x")))
    wrapping_paper += 2*d1*d2 + 2*d1*d3 + 2*d2*d3 + d1*d2
    ribbon += 2*d1 + 2*d2 + d1*d2*d3
    
print(wrapping_paper)
print(ribbon)