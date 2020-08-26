escolha=int(input("Digite um número de 1 a 10: "))
e=escolha
while e<10:
  o=1
  while o<11:
    print(escolha,"x",o,"=",escolha*o)
    o=o+1
    print()
    e=e+1 