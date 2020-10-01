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

def adjacentes(g, v):
    return g[v]

grafo = { }
while True:
    x = input("Entre com o vértice ou FIM para encerrar: ")
    if x=='FIM':
        break
    y = input("Entre com um vértice adjacente:")

    insere_aresta(grafo, x, y)

imprime_grafo(grafo)

def busca_largura(grafo, vertice_fonte):
    
    visitados = []
    
    fila = [vertice_fonte]

    while fila:
        
        vertice = fila.pop(0)
        if vertice not in visitados:
            
            visitados.append(vertice)
            vizinhos = grafo[vertice]
 
            
            for vizinho in vizinhos:
                fila.append(vizinho)
    return visitados

print("="*50)
z = input("Escolha o vértice inicial da busca em largura: ")

print(busca_largura(grafo, z))