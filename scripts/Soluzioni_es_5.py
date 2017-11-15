# -*- coding: utf-8 -*-
"""
Soluzioni Esercitazione 5

Created on Wed Nov 15 09:23:42 2017

@author: gualandi
"""

from pairslist import *

# Soluzione Esercizio 1: controllo se due liste sono uguali
def Equal(As, Bs):
    """ Check if two lists have the same sequence of elements """
    if IsEmpty(As):
        return IsEmpty(Bs)
    # da qui As non è vuota...
    if IsEmpty(Bs):
        return False
    if Head(As) != Head(Bs):
        return False
    return Equal(Tail(As), Tail(Bs))

# Soluzione Esercizio 2: intersezione di due tuple
def IntersectRec(As, Bs):
    """ Intersects the elements in As with the elements in Bs.
        Do not count duplicates elements """
    Rs = ()
    for a in As:
        if a in Bs and a not in Rs:
            Rs = Rs + (a,)
    return Rs

def Intersect(As, Bs):
    """ Intersects the elements in As with the elements in Bs.
        Do not count duplicates elements """
    Rs = ()
    for a in As:
        if a in Bs and a not in Rs:
            Rs = Rs + (a,)
    return Rs

def TestZero(n=1):
    if n == 1:
        # Passa alla funzione due tuple
        if Intersect((2,3,4,2,1,2,7), (2,3,2,3,4)) == (2, 3, 4):
            return 'ok'
    else:
        # Passa alla funzione due liste, ritorna una tupla
        if Intersect([2,3,4,2,1,2,7], [2,3,2,3,4]) == (2, 3, 4):
            return 'ok'
    return 'failed'

# Soluzione Esercizio 3
def RimuoviDuplicati(As, Bs):
    """ Rimuovi dalla lista As ogni elemento che appare anche nella lista Bs
        Modifica As senza costruire una nuova lista """
    Rs = []
    for a in As:
        if a in Bs:
            Rs = Rs + [a]
    for r in Rs:
        As.remove(r)
# Per soluzioni esercizio 4 e 5, lezione del 16/11/2017

# Soluzione Esercizio 6
def PulisciTesto(s, blanks):
    r = s.replace('\n', ' ')
    r = r.replace("'", ' ')
    r = r.replace("\xa0", ' ')
    r = r.replace("\ufeff", ' ')
    for c in blanks:
        r = r.replace(c,'')
    return r

def ContaCaratteri(s):    
    D = {}          # Costruttore di un dizionario vuoto
    for c in s:     # Ciclo su tutti caratteri della stringa
        if c in D:
            D[c] += 1
        else:
            D[c] = 1
    return D

def CalcolaFrequenza(D):
    F = {}
    tot = sum(D.values())
    # Soluzione semplice
    for key in D:
       F[key] = round(D[key]/tot*100, 3)
    # Soluzione alternativa (DA SPIEGARE!)
    #F = dict(map(lambda key: (key,round(D[key]/tot*100,3)), D))
    return F

def TestFrequenze(filename):
    fh = open(filename, 'r', encoding="utf-8")
    s = fh.read()
    # Pulisce la stringa letta
    #r = PulisciTesto(s, ',?\n”“')
    r = PulisciTesto(s, ',?\n”“ ’!&".$()/:_-;@*0123456789#%[]«»„à—')
    Cs = ContaCaratteri(r.lower())
    Fs = CalcolaFrequenza(Cs)
    
    # Pretty print a table
    print('\n\t\tTABELLA DELLE FREQUENZE (perecentuali)')
    for i,key in enumerate(sorted(Fs)):
        c = '\n' if (i+1)%5 == 0 else '\t\t'
        print("{1}={0:.2f}".format(Fs[key], key),sep='',end=c)
    print()
    return Fs


# Soluzione Esercizio 7
def ComputeTables(Ls):
    char2int, int2char, idx = {}, {}, 0
    for key in sorted(Ls):  # Lista di chiavi, ordine sulle chiavi
        char2int[key] = idx
        int2char[idx] = key
        idx = idx + 1        
    return char2int, int2char

#-----------------------------------------------
# MAIN function per testare tutte le soluzioni
#-----------------------------------------------
if __name__ == "__main__":
    # Test per esercizio 1
    As = MakeRange(1,10)
    Bs = MakeRange(1,10)
    Cs = MakeRange(2,3)
    print(As)
    print(Bs)
    print(Cs)
    print('As == Bs:', Equal(As,Bs))
    print('As == Cs:', Equal(As,Cs))
    print('Bs == Cs:', Equal(Bs,Cs))
    
    # Test per esercizio 3
    print('Test zero: '+TestZero())
    
    # Test per esercizio 3
    L1 = [2, 4, 2, 5, 6, 6, 3, 2, 9, 4]
    L2 = [2, 4, 7]
    RimuoviDuplicati(L1, L2)
    print('L1 =', L1)
    
    # Test per esercizio 6
    TestFrequenze('../data/canzone.txt')
    Fs = TestFrequenze('../data/LeAvventureDiPinocchio.txt')
    
    # Test per esercizio 7
    char2int, int2char = ComputeTables(Fs)
    print('Codifica char2int: {}={}'.format('g', char2int['g']))
    print('Codifica int2char: {}={}'.format(13, int2char[13]))
    print('Codifica char2int: {}={}'.format('n', char2int['n']))
