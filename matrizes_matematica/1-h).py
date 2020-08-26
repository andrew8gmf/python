import numpy as np
import random

print("\nProduto entre matrizes\n")

while True:
	mA = int(input("Linhas de A: "))
	nA = int(input("Colunas de A: "))
	x=mA*nA
	matrizA = np.arange(x).reshape(mA,nA)

	mB = int(input("\nLinhas de B: "))
	nB = int(input("Colunas de B: "))
	y=mB*nB
	matrizB = np.arange(y).reshape(mB,nB)
	
	if (nA!=mB):
		print("\n\nNúmero de colunas da Matriz A diferente do número de linhas da Matriz B\n")
	else:	
		break

#A
for i in range(mA):
	for j in range(nA):
		matrizA[i][j] = random.randint(0,9)

print("\nMatriz A")
for i in range(mA):
	for j in range(nA):
		print(matrizA[i][j], end=" ")
	print()
print()

#B
for i in range(mB):
	for j in range(nB):
		matrizB[i][j] = random.randint(0,9)

print("Matriz B")
for i in range(mB):
	for j in range(nB):
		print(matrizB[i][j], end=" ")
	print()
print()

#C
z=mA*nB
matrizC = np.arange(z).reshape(mA,nB)

for i in range(mA):
	for j in range(nB):
		prod = 0
		for k in range(mB):
			prod += matrizA[i][k] * matrizB[k][j]
		matrizC[i][j] = prod

print("Produto das matrizes")
for i in range(mA):
	for j in range(nB):
		print(matrizC[i][j], end=" ")
	print()