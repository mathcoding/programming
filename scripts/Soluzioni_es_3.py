# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 00:11:28 2017

@author: gualandi
"""

# Esercizio 3.1: Accumula
def AccumulaRec(Op, EN, F, a, Next, b):
    if a > b:
        return EN
    return Op(F(a), AccumulaRec(Op, EN, F, Next(a), Next, b))

def AccumulaIter(Op, EN, F, a, Next, b):
    def AccI(accumulator, v):
        if v > b:
            return accumulator
        return AccI(Op(accumulator, F(v)), Next(v))
    return AccI(EN, a)

# Decidi quale versione di Accumula usare nelle prossime funzioni
Accumula = AccumulaRec

def Sommatoria(F, a, Next, b):
    def Add(x, y):
        return x+y
    return Accumula(Add, 0, F, a, Next, b) 


def Produttoria(F, a, Next, b):
    def Mul(x, y):
        return x*y
    return Accumula(Mul, 1, F, a, Next, b) 


# Funzioni di supporto per il test
def Integrale(F, a, b, dx):
    def AddDx(x):
        return x + dx
    return dx*Sommatoria(F, a+dx/2, AddDx, b)

def Cubo(x):
    return x**3


# Esercizio 3.2: Filtra e accumula
def FiltraAccumula(P, Op, EN, F, a, Next, b):
    def FAI(accumulator, v):
        if v > b:
            return accumulator
        if P(v):
            return FAI(Op(accumulator, F(v)), Next(v))
        return FAI(accumulator, Next(v))
    return FAI(EN, a)

def IsPrime(n):
    """ Predicato che restituisce "True" quando "n" è un numero primo """
    def MinorDivisore(a, n):
        if a*a > n:
            return n
        if n % a == 0:
            return a
        return MinorDivisore(a+1, n)
    
    if n == 0:
        return False
    if n == 1:
        return True
    return MinorDivisore(2,n) == n


#-----------------------------------------------
# MAIN function per testare tutte le soluzioni
#-----------------------------------------------
if __name__ == "__main__":
    print("Es. 3.1.b => Confronto per IntegraleIter(1, 5): ", Integrale(Cubo, 0, 1, 0.05))
    print("Es. 3.1.c => Confronto per ProduttoriaRec(1, 5): ", Produttoria(lambda x: x, 1, lambda z: z+1, 5))
    
    print("Es. 3.2 => Quadrato dei numeri primi in [1,5]: ", 
          FiltraAccumula(IsPrime, lambda x,y: x+y, 0, lambda z: z**2, 1, lambda z: z+1, 5))