# -*- coding: utf-8 -*-
"""
Soluzioni Esercitazione 6

Created on Tue Nov 28 20:57:35 2017

@author: gualandi
"""

# Esercizio 1
def IsSet(Ls, P=lambda x,y: x == y):
    def InnerCheck(a, Bs):
        for b in Bs:
            if P(a, b):
                return False
        return True
    
    def OuterCheck(As):
        if As == []:
            return True
        if not InnerCheck(As[0], As[1:]):
            return False
        return OuterCheck(As[1:])
    
    return OuterCheck(Ls)
                
# Soluzione alternativa
def IsSetAlt(Ls, P=lambda x,y: x == y):
    for i,a in enumerate(Ls):
        for b in Ls[i+1:]:
            if P(a,b):
                return False
    return True
    

# Esercizio 2
def Insert(As, value, i):
    # L'esercizio si poteva risolvere studiando la documentazione di Python
    As.insert(i, value)
    # NOTA: in questo caso però veniva modificata la lista passata in input
    
def InsertAlt(As, value, i):
    # In questo caso viene creata una nuova lista, con una copia di tutti gli 
    # elementi, più l'inserimento dell'elemento da aggiungere
    return As[:i] + [value] + As[i:]
    

# Esercizio 3
def InsertOrder(As, z, Cmp=lambda x,y: x < y):
    if Cmp(z, As[0]):
        return [z] + As
    if Cmp(As[-1], z):
        return As + [z]
    i = 1
    for a,b in zip(As[:-1], As[1:]):
        if Cmp(a,z) and Cmp(z,b):
            return As[:i] + [z] + As[i:]
        i = i + 1
    return As

    
# Esercizio 4
def Contains(As, z):
    a = 0
    b = len(As)-1
    mid = a+(b-a)//2

    while a < mid and mid < b:
        if As[mid] == z:
            return True
        if As[mid] < z:
            a = mid            
        else:
            b = mid
        mid = a+(b-a)//2
              
    return As[a] == z or As[b] == z
    

# Esercizio 5
from functools import reduce
def DotProduct(As, Bs):
    # NOTA: reduce è equivalente a un FoldRight
    return reduce(lambda x,y: y[0]*y[1]+x, zip(As,Bs), 0)

def MatrixVector(A, v):
    return list(map(lambda x: DotProduct(x,v), A))

def MatrixMatrix(A, B):
    return [MatrixVector(A,v) for v in B]
        
def Transpose(A):
    if A[0] == []:
        return []
    return [list(map(lambda x: x[0], A))] + Transpose(list(map(lambda x: x[1:], A)))
    

#-----------------------------------------------
# MAIN function per testare tutte le soluzioni
#-----------------------------------------------
if __name__ == "__main__":
    # Test per esercizio 1
    print("IsSet([2,3,6,4,2]): ", IsSet([2,3,6,4,2]))
    print("IsSet([2,3,7,4,5]): ", IsSet([2,3,7,4,5]))
    
    print("IsSetAlt([2,3,6,4,2]): ", IsSetAlt([2,3,6,4,2]))
    print("IsSetAlt([2,3,7,4,5]): ", IsSetAlt([2,3,7,4,5]))
    print()
    
    # Test per esercizio 2
    Ls = [0,1,2,3,5]
    print("Ls prima:", Ls)
    Insert(Ls, 9, 3)
    print("Ls dopo:", Ls)
    Bs = InsertAlt(Ls, 9, 3)
    print("Soluzione alternativa:", Bs)
    print("Oggetti diversi: {}, {}".format(id(Ls), id(Bs)))
    print()
    
    # Test per esercizio 3
    Cs = sorted(Ls)
    print("Test insert ordinato:", InsertOrder(Cs, 7))
    print("Test insert ordinato:", InsertOrder(Cs, 2))
    print("Test insert ordinato:", InsertOrder(Cs, 4))
    print("Test insert ordinato:", InsertOrder(Cs, -2))
    
    # Test per esercizio 4
    print("Contains: ", Contains([1,3,4,6,7,9,10,14,15,23], 12))
    print("Contains: ", Contains([1,3], 3))
    print("Contains: ", Contains([1,3,4,6,7,9,10,14,15,23], 4))

    # Test per Eserczio 5
    print(DotProduct([1,2,3],[3,2,1]))
    print(MatrixVector([[1,2,3],[1,0,1]], [2,1,1]))
    print(MatrixMatrix([[1,2,3],[1,0,1]], [[2,1,1],[0,0,1]]))
    print(Transpose([[1,2,3],[1,0,1]]))