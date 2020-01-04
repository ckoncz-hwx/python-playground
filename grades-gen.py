import sys
import random

if len(sys.argv) != 4:
    print('provide N K L on the command line')
    sys.exit(1)

N, K, L =(int(i) for i in sys.argv[1:4])
print(N, K, L)

limits = [int(K*(i+1)/5) for i in range(4)]
print(*limits)

first = True
for i in range(N):
    if first:
        first = False
    else:
        print(' ', end='')
    print(random.randint(1,K), end='')
print()