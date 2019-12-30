from sys import stdin, stdout
import math

s = int(stdin.readline())

p1 = (50+math.sqrt(2500-200*s))/2
if (p1>30):
    p1=""
p2 = (50-math.sqrt(2500-200*s))/2
if (p2>30):
    p2=""

print(p1,p2)