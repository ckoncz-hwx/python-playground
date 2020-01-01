from sys import stdin, stdout
from typing import Dict, List

print("bemenet")
elso = [int (i) for i in stdin.readline().split()]
adat = []
for i in range(elso[1]):
    adat.append([int (i) for i in stdin.readline().split()])
print(adat)

nodes: Dict[int, List[int]] = {}
end_nodes = []

for edge in adat:
    start = edge[0]
    end = edge[1]
    
    if not start in nodes.keys():
        nodes[start] = []
    nodes[start].append(end)
    
    if not end in end_nodes:
        end_nodes.append(end)
    
start_nodes = nodes.keys() - end_nodes
print(nodes)
print(start_nodes)

def find(nodes: Dict[int, List[int]], path: List[int]) -> List[List[int]]:
    cycles = []
    n = path[-1]
    if n in nodes.keys():
        targets = nodes[n]
        for t in targets:
            if t in path:
                cycle = path[path.index(t):len(path)]
                append_cycle(cycles,cycle)
            else:
                next_cycles = find(nodes, path+[t])
                for c in next_cycles:
                    append_cycle(cycles,c)
    return cycles

def append_cycle(cycles: List[List[int]], cycle: List[int]):
    cycles.append(cycle)
            
result = []
for i in start_nodes:
    res = find(nodes, [i])
    for i in res:
        result.append(i)
print(result)
