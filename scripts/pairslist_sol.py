# -*- coding: utf-8 -*-
"""
Libreria per la gestione di liste create usando una catena di coppie

@author: gualandi
"""

from pairslist_impl import Head, Tail, EmptyList, MakeList
#from pairslist_array import Head, Tail, EmptyList, MakeList

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

from random import seed, randint
# Inizializza il generatore di numeri casuali
seed(13)
def MakeRandomInts(n, a, b):
    """ Restituisce una lista n di numeri causali, uniformente distribuiti
        nell'intervallo [a,b] (estremi compresi) """
    if n == 0:
        return EmptyList()
    return MakeList(randint(a,b), MakeRandomInts(n-1, a, b))


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

def Contains(As, value):
    """ Controlla se la lista As contiene un elemento pari a 'value' """
    if IsEmpty(As):
        return False
    if Head(As) == value:
        return True
    return Contains(Tail(As), value)

def Count(As, value):
    """ Conta il numero di elementi pari a 'value' nella lista As """
    def CountI(Ls, counter):
        if IsEmpty(Ls):
            return counter
        if Head(Ls) == value:
            return CountI(Tail(Ls), counter+1)
        return CountI(Tail(Ls), counter)
    
    return CountI(As, 0)

def RemoveFirst(As, value):
    """ Rimuovi il primo elemento di 'value' trovato in As """
    if IsEmpty(As):
        return As
    if Head(As) == value:
        return Tail(As)
    return MakeList(Head(As), RemoveFirst(Tail(As), value))

def RemoveAll(As, value):
    """ Rimuovi tutti gli elementi di 'value' trovato in As """
    if IsEmpty(As):
        return As
    if Head(As) == value:
        return RemoveAll(Tail(As), value)
    return MakeList(Head(As), RemoveAll(Tail(As), value))

def FoldRight(Op, As, z):
    """ Riduci la lista As, applicando ad ogni suo elemento la funzione F()
        e accumulando i risultati tramite l'operazione Op() """
    if IsEmpty(As):
        return z
    return Op(Head(As), FoldRight(Op, Tail(As), z))

def FoldLeft(Op, As, z):
    if IsEmpty(As):
        return z
    return FoldLeft(Op, Tail(As), Op(Head(As), z))
    
Fold = FoldLeft

# SOLUZIONI IN TERMINI DI FOLD (Right)

def FoldLength(Ls):
    """ Lunghezza di una lista in termini di fold """
    return Fold(lambda x,y: 1+y, Ls, 0)

def Sum(As):
    """ Calcola la somma di tutti gli elementi nella lista As """
    def Add(a, b):
        return a+b
    return Fold(Add, As, 0)

def Prod(As):
    """ Calcola la somma di tutti gli elementi nella lista As """
    def Mul(a, b):
        return a*b
    return Fold(Mul, As, 1)

def Min(As):
    """ Più piccolo elemento della lista As """
    return Fold(min, Tail(As), Head(As))

def Max(As):
    """ Più grande elemento della lista As """
    return Fold(max, Tail(As), Head(As))

def FoldMap(F, Ls):
    """ Map in termini di Fold """
    return Fold(lambda x,y: MakeList(F(x), y), Ls, EmptyList())

def FoldFilter(P, Ls):
    """ Filter in termini di Fold """
    return Fold(lambda x,y: MakeList(x, y) if P(x) else y, Ls, EmptyList())

def FoldReverse(Ls):
    """ Reverse in termini di Fold """
    def Concatenate(x, Ls):
        return Append(Ls, MakeList(x))
    return Fold(Concatenate, Ls, EmptyList())
    
#-----------------------------------------------
# MAIN function per testare tutte le soluzioni
#-----------------------------------------------
if __name__ == "__main__":
    Ls = MakeRange(1, 5)
    print("MakeList(7): ", end='')
    PrintList(Ls)
    
    Rs = MakeRandomInts(10, 1, 100)
    print("MakeRandomInts(10, 1, 100): ", end='')
    PrintList(Rs)
    
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
    
    
    print("Contains 4:", Contains(Append(Xs, Xs), 4))
    print("Count 4:", Count(Append(Xs, Xs), 4))
    
    print("Remove first 4:", RemoveFirst(Append(Xs, Xs), 4))
    print("Remove all   4:", RemoveAll(Append(Xs, Xs), 4))

    print("FoldMin:", Min(MakeRange(4, 17)))
    print("FoldMax:", Max(MakeRange(4, 17)))

    print("FoldLength(Ls):", FoldLength(Ls))
    print("FoldMap:", FoldMap(lambda x: x**3, Ls))        
    print("FoldFilter:", FoldFilter(lambda x: x % 2 == 0, Ls))
    print("FoldReverse:", FoldReverse(Ls)) 