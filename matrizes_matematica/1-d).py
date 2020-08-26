import numpy as np
import random

print("\nMatriz Transposta\n")
x = int(input("Ordem da matriz: "))
y=x*x

matriz = np.arange(y).reshape(x,x)

for i in range(x):
	for j in range(x):
		matriz[i][j] = random.randint(0,9)

print(" ")
for i in range(x):
	for j in range(x):
		print(matriz[i][j], end=" ")
	print()

transp = matriz.transpose()
print(" ")
print(transp)