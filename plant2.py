import sys

N, M, K, L = (int(i) for i in sys.stdin.readline().split())
X = int(sys.stdin.readline())

plants_by_age = {}
for i in range(1,N+1):
    plants_by_age[i]=0

def total():
    count = 0
    for i in range(1,N+1):
        count += plants_by_age[i]
    return count

def collect_seeds():
    count = 0
    for i in range(M, M+K):
        count += plants_by_age[i]
    return count
def age_plants(seeds):
    for i in range(N,1,-1):
        plants_by_age[i]=plants_by_age[i-1]
    plants_by_age[1] = seeds

year = 1
seeds = L
while year <= X:
    new_plants = seeds
    age_plants(new_plants)
    total_plants = total()

    print(year, new_plants, total_plants)
    
    seeds = collect_seeds()
    year += 1