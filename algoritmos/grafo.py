def insere_aresta(g, a, b):
    if a not in g:
        g[a]=[]
    if b not in g:
        g[b]=[]
    g[a].append(b)
    g[b].append(a)

def imprime_grafo(g):
    for v,a in g.items():
        print("="*50)
        print('Vertice:', v)
        print('Adjacentes:', a)

# Método que dado um grafo e um vértice, retorne com o seu grau (numero inteiro das arestas incidentes)

def grau(a):
    return len(a)

def adjacentes(g, b):
    return g[x]

def arestas(g, b, c):
    if c in g[x]:
        return "Existe aresta entre eles!"

# Programa principal
grafo = { }
while True:
    x = input("Entre com o vértice ou FIM para encerrar: ")
    if x=='FIM':
        break
    y = input("Entre com um vertice adjacente:")

    insere_aresta(grafo, x, y)

imprime_grafo(grafo)

# Visualizar grau de um vertice
x = input("Digite o vertice que deseja saber o grau:")
if x in grafo:
    print("Grau do vertice", x, " = ", grau(grafo[x]))
else:
    print("Não existe vértice!")

# Visualizar os vertices adjacentes de um determinado vertice
x = input("Digite o vertice que deseja saber seus adjacentes:")
if x in grafo:
    print("Adjacentes do vertice:", x, " = ", adjacentes(grafo, x))
else:
    print("Não existe esse vertice!")

# Verificar se existe aresta entre os vertices
x = input("Digite o primeiro vertice:")
y = input("Digite o segundo vertice:")
if x in grafo and y in grafo:
    print(arestas(grafo, x, y))
else:
    print("Um dos vertices não existe!")