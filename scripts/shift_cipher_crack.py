# -*- coding: utf-8 -*-
"""
SHIFT CIPHER CRACK: programma che decripta una stringa cifrata con uno "shift cipher"

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

    return lambda s: ''.join([Shifter(c) for c in s.lower()])

def CleanText(s, blanks):
    """ Remove useless character """
    r = s.replace('\n', ' ')
    r = r.replace("'", ' ')
    r = r.replace("\xa0", ' ')
    r = r.replace("\ufeff", ' ')
    for c in blanks:
        r = r.replace(c,'')
    return r

def CountChars(s):
    """ Count number of occurence for each char """
    D = {}
    for c in s:
        if c in D:
            D[c] += 1
        else:
            D[c] = 1
    return D

def File2String(filename):
    fh = open(filename, 'r', encoding="utf-8")
    return fh.read()    
    
def ComputeFrequencies(s):
    """ Deduce the letters used in a given text """
    Blanks =',?\n”“ ’!&".$()/:_-;@*0123456789#%[]«»„à—'
    Ds = CountChars(CleanText(s, Blanks).lower())

    Fs = {}
    tot = sum(Ds.values())
    for key in Ds:
       Fs[key] = Ds[key]/tot
    return Fs

def ChiSquare(Os, Es):
    """ Calcola la statistica di ChiSquare tra le frequenze di caratteri osservata
        nel testo di cifrato, e quella di riferimento per la lingua italiana """
    for k in Es:
        if k not in Os:
            Os[k] = 0
    return sum([(Os[k]-Es[k])**2/Es[k] for k in Es])

def BruteForce(s, sigma, char2int, int2char, Es):
    # Massimo numero float rappresentabile sul computer
    import sys
    best_value = sys.float_info.max
    best_offset = 0
    
    for i in range(len(Es)):
        Encoder = MakeCipher(-i, char2int, int2char)
        Ms = Encoder(s)
        Os = ComputeFrequencies(Ms)
        if best_value > ChiSquare(Os, Es):
            best_value = ChiSquare(Os, Es)
            best_offset = i
    
    Encoder = MakeCipher(-best_offset, char2int, int2char)
    print(Encoder(s))
    
#-----------------------------------------------
# MAIN function
#-----------------------------------------------
if __name__ == "__main__":    
    Es = ComputeFrequencies(File2String('./LeAvventureDiPinocchio.txt'))
    sigma = sorted(Es.keys())
    
    # Calcola il mapping da char a int e viceversa
    char2int, int2char = ComputeTables(sigma)
    
    BruteForce(File2String('./testo_segreto_facile.txt'), sigma, char2int, int2char, Es)