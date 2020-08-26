##f, facum, facum', frel, frelacum, frelacum', %, %acum, %acum'
from tabulate import tabulate

def line():
  print('-'*100)

f = []
f.append(6) #posição 0
f.append(8) #posição 1
f.append(5) #posição 2
f.append(1) #posição 3
f.append((f[0]+f[1]+f[2]+f[3])) #posição 4

facum=[]
facum.append(f[0])
facum.append((f[1]+facum[0]))
facum.append((facum[1]+f[2]))
facum.append((facum[2]+f[3]))
facum.append('nulo')

facum2=[]
facum2.append(f[4])
facum2.append((facum2[0]-f[0]))
facum2.append((facum2[1]-f[1]))
facum2.append((facum2[2]-f[2]))
facum2.append('nulo')

frel=[]
frel.append((f[0]/facum2[0]))
frel.append((f[1]/facum2[0]))
frel.append((f[2]/facum2[0]))
frel.append((f[3]/facum2[0]))
frel.append(frel[0]+frel[1]+frel[2]+frel[3])

frelacum=[]
frelacum.append(frel[0])
frelacum.append((frelacum[0]+frel[1]))
frelacum.append((frelacum[1]+frel[2]))
frelacum.append((frelacum[2]+frel[3]))
frelacum.append('nulo')

frelacum2=[]
frelacum2.append(1)
frelacum2.append((frelacum2[0]-frel[0]))
frelacum2.append((frelacum2[1]-frel[1]))
frelacum2.append((frelacum2[2]-frel[2]))
frelacum2.append('nulo')

percent=[]
percent.append((frel[0]*100))
percent.append((frel[1]*100))
percent.append((frel[2]*100))
percent.append((frel[3]*100))
percent.append(100)

percentacum=[]
percentacum.append(percent[0])
percentacum.append((percentacum[0]+percent[1]))
percentacum.append((percentacum[1]+percent[2]))
percentacum.append((percentacum[2]+percent[3]))
percentacum.append('nulo')

percentacum2=[]
percentacum2.append(100)
percentacum2.append((percentacum2[0]-percent[0]))
percentacum2.append((percentacum2[1]-percent[1]))
percentacum2.append((percentacum2[2]-percent[2]))
percentacum2.append('nulo')

print (tabulate([['1',f[0],facum[0], facum2[0], frel[0], frelacum[0], round(frelacum2[0],2), percent[0], percentacum[0], percentacum2[0]], 
['2',f[1],facum[1], facum2[1], frel[1], frelacum[1], round(frelacum2[1],2), percent[1], percentacum[1], percentacum2[1]],
['3',f[2],facum[2], facum2[2], frel[2], frelacum[2], round(frelacum2[2],2), percent[2], percentacum[2], percentacum2[2]],
['4',f[3],facum[3], facum2[3], frel[3], frelacum[3], round(frelacum2[3],2), percent[3], percentacum[3], percentacum2[3]],
['Total',f[4],facum[4], facum2[4], frel[4], frelacum[4], frelacum2[4], percent[4], percentacum[4], percentacum2[4]]], 
headers=["Número de filhos","f","facum","facum'","frel","frelacum","frelacum'","$","%acum","%acum'"]))
line()