def grafo_inicial() :   
    return {       
        'A':{'B':6,'C':4},
         'B':{'A':6,'C':8,'D':9,'E':6},
         'C':{'A':4,'B':8,'D':7,'F':8},
         'D':{'B':9, 'C':7,'E':5,'F':4},
         'E':{'B':6,'D':5,'F':3},
         'F':{'C':8,'D':4,'E':3}  
    }

grafo = grafo_inicial()
caminho = {}
vertice_adj = {}
fila = []

print(grafo_inicial())
inicio = input('Digite o vértice inicial: ')
fim = input('Digite o vértice do destino final: ')

for vertice in grafo:
    caminho[vertice] = float("inf")
    vertice_adj[vertice] = None
    fila.append(vertice)

caminho[inicio] = 0

while fila:
    chave_min = fila[0]
    min_val = caminho[chave_min]
    for n in range(1, len(fila)):
        if caminho[fila[n]] < min_val:
            chave_min = fila[n]  
            min_val = caminho[chave_min]
    atual = chave_min
    fila.remove(atual)
    
    for i in grafo[atual]:
        alternador = grafo[atual][i] + caminho[atual]
        if caminho[i] > alternador:
            caminho[i] = alternador
            vertice_adj[i] = atual

print('O caminho mais curto de '+inicio+' para '+fim+': ')
print(fim, end = '<-')

while True:
    try:
        fim = vertice_adj[fim]
    
        if fim is None:
            print("")
            break
        print(fim, end='<-')
    except:
        print('Esse caminho não existe no grafo!')
        break