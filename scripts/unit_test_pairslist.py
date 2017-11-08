# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:02:53 2017

@author: gualandi
"""

from pairslist import *

from random import seed

#-----------------------------------------------
# MAIN function per testare tutte le soluzioni
#-----------------------------------------------
if __name__ == "__main__":
    #seed(13)
    
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
    
    print("FoldMin:", Min(MakeRange(4, 17)))
    print("FoldMax:", Max(MakeRange(4, 17)))

    print("FoldLength(Ls):", FoldLength(Ls))
    print("FoldMap:", FoldMap(lambda x: x**3, Ls))        
    print("FoldFilter:", FoldFilter(lambda x: x % 2 == 0, Ls))
    print("FoldReverse:", FoldReverse(Ls)) 
    
    As = MakeRange(3,7)
    Bs = MakeRange(3,7)
    Cs = MakeRange(3,9)
    print("1. Are As and Bs equal?", id(As) == id(Bs))
    print("2. Are As and Bs equal?", Equal(As, Bs))
    print("3. Are As and Bs equal?", Equal(As, Cs))
    print("4. Are As and Bs equal?", Equal(Bs, Reverse(Bs)))
    