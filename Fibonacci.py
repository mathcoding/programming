# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 23:13:50 2017

@author: gualandi
"""

# Processo con ricorsione ad albero
def Fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fib(n-1) + Fib(n-2)

# Processo iterativo lineare
def FibIter(a, b, count):
    if count == 0:
        return b
    else:
        return FibIter(a+b, a, count-1)        
    
def FibI(n):
    return FibIter(1, 0, n)