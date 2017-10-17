# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:40:41 2017

@author: gualandi
"""

# Esercizio 1.1: Somma dei quadrati dei due numeri maggiori
def SommaMinimi(a, b, c):
    if a < b and a < c:
        return b*b + c*c
    if b < a and b < c:
        return a*a + c*c
    return a*a + b*b

# Esercizio 1.2: Funzione Somma(x,y) usando solo Inc(x) e Dec(x)
def Inc(x):
    return x+1

def Dec(x):
    return x-1

def SommaRec(x, y):
    if y == 0:
        return x
    else:
        return SommaRec(Inc(x), Dec(y))

def Somma(x, y):
    if x < 0 or y < 0:
        print("Entrambi i numeri devono essere positivi!")
    else:
        return SommaRec(x,y)

# Esercizio 1.3: Funzioni per il metodo di Newton per trovare la radice quadrata
def UgualeTol(x, y, tol=0.001):
    return abs(x - y) < tol

def NewtonMigliora(y, x):
    return (y+x/y)/2

def NewtonIter(y, x):
    if UgualeTol(x, y*y):
        return y
    else:
        return NewtonIter(NewtonMigliora(y, x), x)
    
def RadiceNewton(x):
    return NewtonIter(1, x)

# Esercizio 1.4: Funzioni per il metodo di Newton per trovare la radice cubica
def NewtonCuboMigliora(y, x):
    return (x/(y*y) + 2*y)/3

def NewtonCuboIter(y, x):
    if UgualeTol(x, y*y*y):
        return y
    else:
        return NewtonCuboIter(NewtonCuboMigliora(y, x), x)
    
def RadiceCubicaNewton(x):
    return NewtonCuboIter(1, x)

# Esercizio 1.5:
def CountRadiceBisectionSearch(x, a, b, counter):
    if a > b:
        return -1
    y = (b + a)/2
    if UgualeTol(x, y*y):
        return y, counter
    if y*y < x:
        return CountRadiceBisectionSearch(x, y, b, counter+1)
    else:
        return CountRadiceBisectionSearch(x, a, y, counter+1)
    
def CountRadiceBisection(x):
    return CountRadiceBisectionSearch(x, 1, x, 1)

def CountNewtonIter(y, x, counter):
    if UgualeTol(x, y*y):
        return y, counter
    else:
        return CountNewtonIter(NewtonMigliora(y, x), x, counter+1)
    
def CountRadiceNewton(x):
    return CountNewtonIter(1, x, 1)
    
    
    
# Esercizio 1.6: Massimo comun divisore
def MCD(a, b):
    if b == 0:
        return a
    else:
        return MCD(b, a % b)