from collections import defaultdict

adj = defaultdict(dict)

for line in open("day09.in"):
    a, _ ,b, _, w = line.split()
    adj[a].update({b: int(w)})
    adj[b].update({a: int(w)})
    
n_cities = len(adj)

# We solve the first by backtracking
shortest_path = None
min_distance_found = float('inf')
S = [{'visited': [city], 'total_distance': 0} for city in adj]

while S:
    s = S.pop()
    
    if len(s['visited']) == n_cities and s['total_distance'] < min_distance_found:
        shortest_path = s['visited']
        min_distance_found = s['total_distance']
        continue
    
    for city, distance in adj[s['visited'][-1]].items():
        if city not in s['visited'] and (new_distance := s['total_distance'] + distance) < min_distance_found:
            S.append({'visited': s['visited'] + [city], 'total_distance': new_distance})
            
print("Minimum-distance path:")
print("======================")
print(" -> ".join(shortest_path), f"({min_distance_found})")
print()


# We solve the second by brute force
longest_path = None
max_distance_found = float('-inf')
S = [{'visited': [city], 'total_distance': 0} for city in adj]

while S:
    s = S.pop()
    
    if len(s['visited']) == n_cities and s['total_distance'] > max_distance_found:
        longest_path = s['visited']
        max_distance_found = s['total_distance']
        continue
    
    for city, distance in adj[s['visited'][-1]].items():
        if city not in s['visited']:
            S.append({'visited': s['visited'] + [city], 'total_distance': s['total_distance'] + distance})
        
print("Maximum-distance path:")
print("======================")
print(" -> ".join(longest_path), f"({max_distance_found})")