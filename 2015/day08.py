import re

total_length = 0
for line in open("day08.in"):
    line = line.strip()
    code_length = len(line)
    
    memory_length = len(line) - 2
    memory_length -= len(re.findall(r"\\\\", line))
    memory_length -= len(re.findall(r"\\\"", line))
    memory_length -= 3 * len(re.findall(r"\\x[0-9a-f][0-9a-f]", line))
    total_length += code_length
    total_length -= memory_length
    print(line, code_length, memory_length)

print(total_length)