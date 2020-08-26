import numpy as np
import random

print("\nSubtração de matrizes\n")
x = int(input("Ordem das matrizes: "))
y=x*x

matrizA = np.arange(y).reshape(x,x)

for i in range(x):
	for j in range(x):
		matrizA[i][j] = random.randint(0,9)

print("\n\nMatriz A: \n")
for i in range(x):
	for j in range(x):
		print(matrizA[i][j], end=" ")
	print()

matrizB = np.arange(y).reshape(x,x)

for i in range(x):
	for j in range(x):
		matrizB[i][j] = random.randint(0,9)

print("\n\nMatriz B: \n")
for i in range(x):
	for j in range(x):
		print(matrizB[i][j], end=" ")
	print()

subtracao = np.subtract(matrizA,matrizB)
print("\n\nMatriz A - Matriz B: \n")
print(subtracao)