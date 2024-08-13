import re

# Part 1

print(sum(
    1
    for line
    in open("day05.in")
    if (
        len(re.findall(r"[aeiou]", line)) >= 3      # at least three vowels
        and re.findall(r"(.)\1", line)              # at least one letter repeated twice in a row
        and not re.findall(r"ab|cd|pq|xy", line)    # does not contain ab, cd, pq, or xy
    )
))

# Part 2

print(sum(
    1
    for line
    in open("day05.in")
    if (
        re.findall(r"(.)(.).*\1\2", line)           # any repeated non-overlapping pair
        and re.findall(r"(.).\1", line)             # at least one letter that repeats with exactly one letter between them
    )
))
