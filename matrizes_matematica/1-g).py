import numpy as np
import random

print("\nMultiplicação de constante por matriz \n")
m = int(input("Número de linhas: "))
n = int(input("Número de colunas: "))
k = int(input("Digite o valor da constante: "))
x=m*n

matriz = np.arange(x).reshape(m,n)

for i in range(m):
	for j in range(n):
		matriz[i][j]= random.randint(0,9)

print()
print("Matriz")
for i in range(m):
	for j in range(n):
		print(matriz[i][j], end=" ")
	print()
print()

print("Matriz x", k)
for i in range(m):
	for j in range(n):
		matriz[i][j]*= k


for i in range(m):
	for j in range(n):
		print(matriz[i][j], end=" ")
	print()