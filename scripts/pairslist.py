# -*- coding: utf-8 -*-
"""
Libreria per la gestione di liste create usando una catena di coppie

@author: gualandi
"""

from pairlists_impl import Head, Tail, EmptyList, MakeList


def PrintList(As):
    """ Pretty print for a list of elements """
    def PrintListI(As):
        if not IsEmpty(As):
            print(Head(As), end='')
            if not IsEmpty(Tail(As)):            
                print(', ', end='')
            PrintListI(Tail(As))
    print('{', end='')
    PrintListI(As)
    print('}')    

def IsEmpty(As):
    """ Controlla se As è una lista vuota """
    return As == EmptyList()

def MakeRange(a, b):
    """ Restituisce la lista di numeri interi compresi tra 1 e n """
    def MakeI(n):
        if n > b:
            return EmptyList()
        return MakeList(n, MakeI(n+1)) 

    if b < 1:
        print("RuntimeError: Il numero n deve essere maggiore o uguale a 1")
        return EmptyList

    return MakeI(a)

def Nth(As, i):
    """ Restituisce l'i-esimo elemento della lista As """
    if IsEmpty(As):
        return As
    if i == 0:
        return Head(As)
    return Nth(Tail(As), i-1)

def Length(As):
    """ Restituisce il numero di elementi contenuto nella lista As """
    def LengthI(Ls, n):
        if IsEmpty(Ls):
            return n
        return LengthI(Tail(Ls), n+1)
    return LengthI(As, 0)

def Append(As, Bs):
    """ Aggiungi la lista Bs in coda alla lista As """
    if IsEmpty(As):
        return Bs
    return MakeList(Head(As), Append(Tail(As), Bs))

def Scala(As, a):
    """ Restituisci una nuova lista che per ogni elemento di As
        contiene lo stesso valore moltiplicato per 'a' """
    if IsEmpty(As):
        return As
    return MakeList(a*Head(As), Scala(Tail(As), a))

def Quadrati(As):
    """ Restituisci una nuova lista che per ogni elemento di As
        contiene lo stesso valore al quadrato """
    if IsEmpty(As):
        return As
    return MakeList(Head(As)*Head(As), Quadrati(Tail(As)))
    
def Map(F, As):
    """ Restituisci una nuova lista che per ogni elemento di As
        contiene il valore ottenuto applicato F() ad all'elemento """
    if IsEmpty(As):
        return As
    return MakeList(F(Head(As)), Map(F, Tail(As)))

def Filter(P, As):
    """ Restituisci una nuova lista che contiene solo gli elementi di As
        che soddisfano il predicato P() """
    if IsEmpty(As):
        return As
    if P(Head(As)):
        return MakeList(Head(As), Filter(P, Tail(As)))
    return Filter(P, Tail(As))
        
def Reverse(As):
    """ Restituisci una nuova lista gli elemento di As in ordine inverso """
    def ReverseI(Ls, Rs):
        if IsEmpty(Tail(Ls)):
            return MakeList(Head(Ls), Rs)
        return ReverseI(Tail(Ls), MakeList(Head(Ls), Rs))
    return ReverseI(Tail(As), MakeList(Head(As)))


#-----------------------------------------------
# MAIN function per testare tutte le soluzioni
#-----------------------------------------------
if __name__ == "__main__":
    Ls = MakeRange(1, 5)
    
    print("MakeList(7): ", end='')
    PrintList(Ls)
    
    Cs = MakeRange(3,7)
    print("MakeRange(3,7): ", end='')
    PrintList(Cs)

    print("Head(Ls):", Head(Ls))
    print("Tail(Ls):", Tail(Ls))
    
    print("Nth(Ls, 5):", Nth(Ls, 5))
    
    print("Length(Ls):", Length(Ls))

    Bs = MakeRange(1, 3)
    print("Append:", Append(Ls, Bs))
    
    print("Scala:", Scala(Bs, 0.5))
    print("Quadrati:", Quadrati(Bs))
        
    print("Map:", Map(lambda x: x**3, Ls))        
    print("Filter:", Filter(lambda x: x % 2 == 0, Ls))
    
    print("Reverse:", Reverse(Ls))    
    
    print("Reverse:", Sum(Ls))
    Xs = MakeRange(1, 5)
    print("Reverse:", Prod(Xs))
    PrintList(Xs)