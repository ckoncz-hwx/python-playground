from sys import stdin, stdout
import math

lista = [int (i) for i in stdin.readline().split()]
n = lista[0]
t = lista[1]
s = lista[2]

p1 = (50+math.sqrt(2500-200*s))/2
if (p1>30):
    p1= None
p2 = (50-math.sqrt(2500-200*s))/2
if (p2>30):
    p2= None

print(p1,p2)