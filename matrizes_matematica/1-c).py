import numpy as np
import random

print("\nMatriz Simétrica\n")
x = int(input("Ordem da matriz: "))
y=x*x

matriz = np.arange(y).reshape(x,x)

for i in range(x):
	for j in range(x):
		matriz[i][j] = matriz[j][i] = random.randint(0,9)
  
print(" ")
for i in range(x):
	for j in range(x):
		print(matriz[i][j], end=" ")
	print()