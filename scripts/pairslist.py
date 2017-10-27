# -*- coding: utf-8 -*-
"""
Libreria per la gestione di liste create usando una catena di coppie

@author: gualandi
"""

def MakeList(n):
    """ Restituisce la lista di numeri interi compresi tra 1 e n """
    def MakeI(a):
        if a == n:
            return (a, None)
        return (a, MakeI(a+1)) 

    if n < 1:
        print("RuntimeError: Il numero n deve essere maggiore o uguale a 1")
        return None

    return MakeI(1)

def Head(As):
    """ Restituisce il primo elemento della lista As """
    return As[0]

def Tail(As):
    """ Restituisce il secondo elemento della lista As """
    return As[1]

def Nth(As, i):
    """ Restituisce l'i-esimo elemento della lista As """
    if i == 0:
        return Head(As)
    return Nth(Tail(As), i-1)

def Length(As):
    """ Restituisce il numero di elementi contenuto nella lista As """
    def LengthI(As, x):
        if As == None:
            return x
        return LengthI(Tail(As), x+1)
    return LengthI(As, 0)


# DA COMPLETARE:
def MakeRange(a, b):
    return None

def Append(As, Bs):
    return None

def Scala(As, a):
    return None

def Quadrati(As):
    return None
    
def Map(F, As):
    return None

def Filter(P, As):
    return None
    
def Reverse(As):
    return None


#-----------------------------------------------
# MAIN function per testare tutte le soluzioni
#-----------------------------------------------
if __name__ == "__main__":
    Ls = MakeList(7)
    
    print("MakeList(7):", Ls)
    
    print("Head(Ls):", Head(Ls))
    print("Tail(Ls):", Tail(Ls))
    
    print("Nth(Ls, 5):", Nth(Ls, 5))
    
    print("Length(Ls):", Length(Ls))

    Bs = MakeList(3)
    print("Append:", Append(Ls, Bs))
    
    print("Scala:", Scala(Bs, 0.5))
    print("Quadrati:", Quadrati(Bs))
    
    print("Map:", Map(lambda x: x**3, Ls))
    
    print("Filter:", Filter(lambda x: x % 2 == 0, Ls))
    
    print("Reverse:", Reverse(Ls))