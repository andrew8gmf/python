# insere na lista
def Push(P, topo, v):
    P.insert (topo,v)

# pop remove o ultimo elemento da pilha
def Pop(P):
    P.pop()

P = []*50
topo = 0

palavra = input("Digite uma palavra: ")

for letra in palavra:
    Push(P, topo, letra)
    topo += 1

inv = ''

while (topo>0):
    topo -=1
    inv += P[topo]
    Pop(P)

print("Palavra: ", palavra)
print("Palavra invertida: ", inv)

if (palavra==inv):
    print("São palindromos")
else:
    print("Não são palindromos")