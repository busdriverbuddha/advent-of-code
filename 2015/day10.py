from itertools import groupby

def transform(text):
    return "".join(f"{len(list(g))}{k}" for k, g in groupby(text))

with open("day10.in") as f:
    original_text = f.read().strip()
    
text = original_text
for _ in range(40):
    text = transform(text)

print(len(text))

text = original_text
for _ in range(50):
    text = transform(text)

print(len(text))