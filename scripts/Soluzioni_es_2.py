# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 08:43:23 2017

@author: gualandi
"""

# Esercizio 2.1: Calcolo dell'ennesimo numero della sequenza di Fibonacci
#                con un processo iterativo
def FibRec(n):
    """ Calcolo di Fibonacci con PROCESSO RICORSIVO """
    if n == 0 or n == 1:
        return n
    return FibRec(n-1) + FibRec(n-2)

def FibIter(n):
    """ Calcolo di Fibonacci con PROCESSO ITERATIVO """
    def FibI(a, b, counter):
        if counter < 2:
            return a
        return FibI(a+b, a, counter-1)
    
    return FibI(1, 0, n)


# Esercizio 2.2: Vedi teso dell'esercizio per la definizione di F(n)
def FnRec(n):
    """ Calcolo di f(n)  = f(n-1)+2*f(n-2)+3*f(n-3), con f(0)=0, f(1)=1, f(2=2) 
        (uso di processo ricorsivo) """
    if n < 3:
        return n
    return FnRec(n-1) + 2*FnRec(n-2) + 3*FnRec(n-3)

def FnIter(n):
    """ Calcolo di f(n)  = f(n-1)+2*f(n-2)+3*f(n-3), con f(0)=0, f(1)=1, f(2=2) 
        (uso di processo iterativo) """
    def FnI(a, b, c, counter):
        if counter < 3:
            return a
        return FnI(a+2*b+3*c, a, b, counter-1)
    
    return FnI(2, 1, 0, n)

# Esercizio 2.3: Controllare che dato numero sia un numero primo
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

# Esercizio 2.4: Procedura "Sommatoria" come processo iterativo lineare
def SommatoriaRec(F, a, Next, b):
    if a > b:
        return 0
    else:
        return F(a) + SommatoriaRec(F, Next(a), Next, b)

def SommatoriaIter(F, a, Next, b):
    def SommatoriaI(a, b, accumulator):
        if a > b:
            return accumulator
        return SommatoriaI(Next(a), b, accumulator+F(a))
    
    return SommatoriaI(a, b, 0)
    
def Inc(x):
    return x+1

def Cubo(x):
    return x**3

def IntegraleRec(F, a, b, dx):
    def AddDx(x):
        return x + dx
    return dx*SommatoriaRec(F, a+dx/2, AddDx, b)

def IntegraleIter(F, a, b, dx):
    def AddDx(x):
        return x + dx
    return dx*SommatoriaIter(F, a+dx/2, AddDx, b)

# Esercizio 2.5: Procedura "Produttoria" 
def ProduttoriaRec(F, a, Next, b):
    if a > b:
        return 1
    else:
        return F(a) * ProduttoriaRec(F, Next(a), Next, b)

def Fattoriale(n):
    if n == 1:
        return 1
    else:
        return n * Fattoriale(n-1)

# Controllo esercizio 2.6
# Importo dalla libreria solo gli oggetti che mi servono veramente
from numpy import linspace
from matplotlib.pyplot import plot, xlabel, ylabel, show, legend, clf
from math import log
    
def PlotFunzioni():   
    D = linspace(1, 10, 100)
    clf()
    #plot(D, [x for x in D], label="y=x")
    plot(D, [x*x for x in D], label="y=x^2")
    plot(D, [log(x) for x in D], label="y=log(x)")
    plot(D, [x*log(x) for x in D], label="y=x*log(x)")
    
    #D = linspace(1, 10, 100)
    #plot(D, [1.6**x for x in D], label="y=1.6^x")
    #plot(D, [2**x for x in D], label="y=2^x")
    xlabel("x")
    ylabel("y=f(x)")
    legend(loc="upper left", shadow=True)
    show()

    
#-----------------------------------------------
# MAIN function per testare tutte le soluzioni
#-----------------------------------------------
if __name__ == "__main__":
    # Controllo esercizio 2.1
    print("Es. 2.1 => Confronto per Fib(9): ", FibIter(10), " = ", FibRec(10))
    print()
    
    # Controllo esercizio 2.2
    print("Es. 2.2 => Confronto per f(10): ", FnRec(10), " = ", FnIter(10))
    print()
    
    # Controllo esercizio 2.3
    print("Es. 2.3 => Confronto per IsPrime(13): ", IsPrime(13))
    print("Es. 2.3 => Confronto per IsPrime(15): ", IsPrime(15))
    print("Es. 2.3 => Numeri da 0 a 19: ", [(i, IsPrime(i)) for i in range(20)])
    print()
    
    # Controllo esercizio 2.4
    print("Es. 2.4 => Confronto per SommatoriaRec(1, 5): ", SommatoriaRec(Cubo, 1, Inc, 5))
    print("Es. 2.4 => Confronto per SommatoriaIter(1, 5): ", SommatoriaIter(Cubo, 1, Inc, 5))
    print("Es. 2.4 => Confronto per IntegraleRec(1, 5): ", IntegraleRec(Cubo, 0, 1, 0.05))
    print("Es. 2.4 => Confronto per IntegraleIter(1, 5): ", IntegraleIter(Cubo, 0, 1, 0.05))
    print()
    
    # Controllo esercizio 2.5
    print("Es. 2.5 => Confronto per ProduttoriaRec(1, 5): ", ProduttoriaRec(lambda x: x, 1, Inc, 5))
    print("Es. 2.5 => Confronto per Fattoriale(5): ", Fattoriale(5))
    print()

    # Controllo esercizio 2.6
    print("Es. 2.6 => Vedi finestra a parte")
    PlotFunzioni()    