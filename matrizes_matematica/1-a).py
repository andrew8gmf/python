import numpy as np
import random

print("\nMatriz Diagonal\n")
x = int(input("Ordem da matriz: "))
y=x*x

matriz = np.arange(y).reshape(x,x)

for i in range(x):
	for j in range(x):
		if i==j:
			matriz[i][j] = random.randint(1,9)
		else:
			matriz[i][j]=0

print(" ")
for i in range(x):
	for j in range(x):
		print(matriz[i][j], end=" ")
	print()