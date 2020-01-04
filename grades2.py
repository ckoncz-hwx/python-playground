from sys import stdin
from typing import Set, List

N, K, L = (int(i) for i in stdin.readline().split())
limits = [int(i) for i in stdin.readline().split()]
student_scores = [int(i) for i in stdin.readline().split()]

scores: Set[int] = set()

for s in student_scores:
    scores.add(s)

scores_list = list(scores)
scores_list.sort(reverse=True)
limits.reverse()

idx = 0
score = scores_list[0]
new_limits: List[int] = []
for l in limits:
    new_limit = l
    while score >= l and idx < (len(scores_list)-1):
        idx += 1
        score = scores_list[idx]
    
    while score == new_limit-1 and l - new_limit < L:
        new_limit -= 1
        if idx < (len(scores_list)-1):
            idx += 1
            score = scores_list[idx]
    
    if l - new_limit == L:
        if score == new_limit -1:
            # we have to reset the new limit:
            new_limit = l

    new_limits.append(new_limit)

new_limits.reverse()
for i in new_limits:
    print(i)
    

    