from sys import stdin
from typing import Tuple, List

print("enter family data:")

members=int(stdin.readline())

parents={}
for child in range(2, members+1):
    parent = int(stdin.readline())
    if parent not in parents:
        parents[parent]=[]
    parents[parent].append(child)

# print(parents)

def find(parent,level)->Tuple[int,List[int]]:
    if not parent in parents:
        return 0, []
    
    children=parents[parent]
    deep_level = level
    deep_children = children

    for child in children:
        maxdepth, grand_children = find(child, level+1)
        if maxdepth == deep_level:
            deep_children += grand_children
        elif maxdepth > deep_level:
            deep_level = maxdepth
            deep_children = grand_children

    return deep_level, deep_children

maxdepth, deep_children = find(1,1)
deep_children = deep_children.copy()
deep_children.sort()
print(maxdepth, len(deep_children))
print(" ".join([str(i) for i in deep_children]))