# -*- coding: utf-8 -*-
"""
SHIFT CIPHER: programma che codifica una stringa usando il cifrario di cesare,
              ma con un offset variabile

Cifrario di Cesare:  https://it.wikipedia.org/wiki/Cifrario_di_Cesare

Created on Wed Nov 15 10:32:37 2017
@author: gualandi
"""

def ComputeTables(Ls):
    """ Compute correspondance between alphabet letters and integer codes """
    char2int, int2char, idx = {}, {}, 0
    for key in sorted(Ls):  # Lista di chiavi, ordine sulle chiavi
        char2int[key] = idx
        int2char[idx] = key
        idx = idx + 1        
    return char2int, int2char


def MakeCipher(offset, char2int, int2char):
    """ Return a function that implement a 'shift cipher' """
    def Shifter(x):
        """ Ignore blanks and other chars, but shift all the others """
        if x not in char2int:
            return x
        return int2char[(char2int[x]+offset) % len(int2char)]

    # La funzione join concatena una lista di stringhe in un'unica stringa
    # Esempio: ''.join(['a','b','b']) restituisce la stringa 'abb'
    # Esempio: '#'.join(['a','b','b']) restituisce la stringa 'a#b#b'
    return lambda s: ''.join([Shifter(c) for c in s.lower()])

#-----------------------------------------------
# MAIN function per testare tutte le soluzioni
#-----------------------------------------------
if __name__ == "__main__":    
    sigma = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
             'w', 'x', 'y', 'z', 'à', 'è', 'ì', 'ò', 'ù']
    
    # Calcola il mapping da char a int e viceversa
    char2int, int2char = ComputeTables(sigma)
    
    # Costruisci l'encoder    
    Encoder = MakeCipher(-13, char2int, int2char)
    
    # Leggi file da codificare
    fh = open('./testo_segreto_facile.txt', 'r', encoding="utf-8")
    msg = fh.read()
    print('TESTO DA CIFRARE:\n', msg)
    print('TESTO CIFRATO:\n', Encoder(msg))