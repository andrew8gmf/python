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

grafo = { }
while True:
    x = input("Entre com o vértice ou FIM para encerrar: ")
    if x=='FIM':
        break
    y = input("Entre com um vertice adjacente:")

    insere_aresta(grafo, x, y)

imprime_grafo(grafo)

x = input("Digite o vertice que deseja saber o grau:")
if x in grafo:
    print("Grau do vertice", x, " = ", grau(grafo[x]))
else:
    print("Não existe vértice")