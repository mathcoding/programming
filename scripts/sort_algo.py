# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:23:55 2017

@author: gualandi
"""

from pairslist import IsEmpty, Min, RemoveFirst, MakeList, MakeRandomInts, Head, Tail, Filter, Append

def SelectionSort(As):
    """ Semplice implementazione ricorsiva di selection sort """
    def SortI(Ls):
        if IsEmpty(Ls):
            return Ls
        a = Min(Ls)
        return MakeList(a, SortI(RemoveFirst(Ls, a)))
        
    return SortI(As)

def QuickSort(As, Compare=lambda x,y: x<=y):
    """ Semplice implementazione ricorsiva di quick sort """
    if IsEmpty(As):
        return As
    x = Head(As)
    # ESERCIZIO: Invece di avere queste due funzioni separate, si potrebbe
    #            avere un'unica funzione che restituisce le due liste, ma 
    #            "itera" sulla lista As solo una volta invece di due volte
    Ls = Filter(lambda z: Compare(z, x), Tail(As))
    Gs = Filter(lambda z: not Compare(z, x), Tail(As))
    return Append(QuickSort(Ls, Compare), Append(MakeList(x), QuickSort(Gs, Compare)))

def MergeSort(As):
    """ Semplice implementazione ricorsiva del merge sort """
    # DA FARE COME ESERCIZIO
    pass

#-----------------------------------------------
# MAIN function per testare tutte le soluzioni
#-----------------------------------------------
if __name__ == "__main__":
    import random
    random.seed(13)
    Ls = MakeRandomInts(10, 1, 100)
    print(Ls)
    
    print('Selection sort:', SelectionSort(Ls))
    
    print('Quick sort:', QuickSort(Ls))
    print('Quick sort:', QuickSort(Ls, lambda x,y: x<y))
    
    # Test Di ordinamento di lista di coppie
    Ls = (('b',3), (('a',1), (('c',-10), (('r', 13), None))))
    print('Quick sort:', QuickSort(Ls, lambda x,y: x[0]<y[0]))
    print('Quick sort:', QuickSort(Ls, lambda x,y: x[1]>y[1]))
    
    # ESERCIZIO: Implementare il merge sort
    print('Merge sort:', MergeSort(Ls))
    













