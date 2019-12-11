import browser
from browser import document
import math

lista = [int (i) for i in browser.prompt("Kérem a tyúkinfót").split()]
# lista = [int (i) for i in document['bemenet'].value.split()]
n = lista[0]
t = lista[1]
s = lista[2]

p1 = (50+math.sqrt(2500-200*s))/2
if (p1>30):
    p1=""
p2 = (50-math.sqrt(2500-200*s))/2
if (p2>30):
    p2=""

print(p1,p2)
document.body.innerHTML += "<br>Tyúkeredmény %s %s"%(p1,p2)
