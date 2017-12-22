# -*- coding: utf-8 -*-
"""
ESERCITAZIONE 9: Completare la funzione ShortestPath(G, v, w) in modo che calcoli
                 il cammino minimo da v a w in G. Per la rappresentazione del grafo,
                 usare le classi Vertex, Edge, ListGraph, date sotto.
"""

class Vertex(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __str__(self):
        return "({}, {})".format(self.name, self.value)

    
class Edge(object):
    def __init__(self, v, w):
        self.v = v
        self.w = w
    def __str__(self):
        return '{} -> {}'.format(self.v, self.w)

    
class ListGraph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        
    def addVertex(self, node):
        if node in self.nodes:
            raise ValueError('Nodo già inserito')
        else:
            self.nodes.add(node.value)
            self.edges[node.value] = []
    
    def addEdge(self, edge):
        if edge.v not in self.nodes or edge.w not in self.nodes:
            raise ValueError('Uno dei due estremi non è presente nella lista di nodi')
        self.edges[edge.v].append(edge.w)
        self.edges[edge.w].append(edge.v)
        
    def neighbourOf(self, node_value):
        return self.edges[node_value]
    
    def __str__(self):
        # DA COMPLETARE
        s = 'nodes: {},\nedges: [\n'.format(self.nodes)
        for e in self.edges:
            s += '  {}: {}\n'.format(e, list(map(str, self.edges[e])))
        s += ']'
        return s
         

def TestSP():
    G = ListGraph()
    for i in range(6):
        G.addVertex(Vertex('n'+str(i), i))
        
    for e in [(0,1),(1,2),(2,3),(2,4),(3,4),(3,5),(0,2),(1,0),(3,1),(4,0)]:
        G.addEdge(Edge(e[0], e[1]))
        
    sp = ShortestPath(G, 0, 5)
    print(sp)


# Libreria per leggere un file JSON
import json

# Leggi un grafo in formato JSON
def ReadGraph(filename):
    G = ListGraph()
    with open(filename, 'r', encoding="utf-8") as f:
        Ds = json.load(f)
        for n in Ds['nodes']:
            G.addVertex(Vertex(n['name'], int(n['value'])))
        for e in Ds['links']:
            G.addEdge(Edge(int(e['source']), int(e['target'])))
    
    return G


def ShortestPath(G, v, w):
    # ESERCIZIONE 9: DA COMPLETARE           
    return None

#-----------------------------------------------
# MAIN function
#-----------------------------------------------
if __name__ == "__main__":
    # Decidi prima quale grafo usare per testare la funzione
    if True:
        # Test simile a quello presente nel capitolo 12 del libro
        TestSP()
    else:
        # Test su un sottografo del grafo di starwars    
        G = ReadGraph('../data/starwars_small.json')    
        # Grafo completo: G = ReadGraph('../data/starwars.json') 
        print(G)
        print(ShortestPath(G, 147, 5))
