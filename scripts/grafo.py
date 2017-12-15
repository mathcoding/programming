# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 10:24:34 2017

@author: gualandi
"""

class Vertex(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

    
class Edge(object):
    def __init__(self, v, w):
        self.v = v
        self.w = w
    def __str__(self):
        return self.v + '->' + self.w

    
class ListGraph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}
        
    def addVertex(self, node):
        if node in self.nodes:
            raise ValueError('Nodo già inserito')
        else:
            self.nodes.append(node)
            self.edges[node.name] = []
    
    def addEdge(self, edge):
        if edge.v not in self.nodes or edge.w not in self.nodes:
            raise ValueError('Uno dei due estremi non è presente nella lista di nodi')
        self.edges[edge.v].append(edge)
        self.edges[edge.w].append(edge)
        
    def neighbourOf(self, node):
        return self.edges[node]
    
    def __str__(self):
        # DA COMPLETARE
        return ''
      
def ShortestPath(G, v, w):
    # DA COMPLETARE
    return []
            
#-----------------------------------------------
# MAIN function
#-----------------------------------------------
if __name__ == "__main__":
    G = ListGraph()
    # RIMEPIRE IL GRAFO
    
    # v = ??
    # w = ??
    #print(ShortestPath(G, v, w))