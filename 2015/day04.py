# There is absolutely no reason to reinvent the wheel.

import hashlib

with open("day04.in") as f:
    secret_key = f.read().strip()
    
# Part 1
i = 0    
while True:
    hash_input = f"{secret_key}{i}".encode()
    hexdigest = hashlib.md5(hash_input).hexdigest()
    if hexdigest.startswith("00000"):
        break
    i += 1

print(i)

# Part 2
i = 0    
while True:
    hash_input = f"{secret_key}{i}".encode()
    hexdigest = hashlib.md5(hash_input).hexdigest()
    if hexdigest.startswith("000000"):
        break
    i += 1

print(i)