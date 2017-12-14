# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 06:27:35 2017

@author: gualandi
"""

def SelectItems(Ls, B):
    fobj, weight, sol = 0, 0, []           
    for item in Ls:
        if weight + item[1] <= B:
            fobj = fobj+ item[0]
            weight = weight + item[1]
            sol.append(item)
    return (fobj, sol)                     
    
def KnapsackGreedy(Items, B, OrderFun):
    Ls = filter(lambda x: x[1] <= B, Items)
    Ls = sorted(Ls, key=OrderFun, reverse=True)    
    return SelectItems(Ls, B)
    
    
from itertools import permutations, combinations

def KnapsackCombinations(Items, B):
    Ls = list(filter(lambda x: x[1] <= B, Items))
    
    best, bsol = 0, []
    for k in range(len(Ls)):
        for os in combinations(Ls, k):
            fobj, sol = SelectItems(os, B)
            if fobj > best:
                best = fobj
                bsol = sol
            
    return best, bsol
 
def KnapsackPermutations(Items, B):
    Ls = list(filter(lambda x: x[1] <= B, Items))
    
    best, bsol = 0, []
    for os in permutations(Ls):
        fobj, sol = SelectItems(os, B)
        if fobj > best:
            best = fobj
            bsol = sol
            
    return best, bsol
        
        
#-----------------------------------------------
# MAIN function
#-----------------------------------------------
if __name__ == "__main__":
    Ls = [(175,10),(90,9),(20,4),(50,2),(10,1),(200,20)]
    B = 20
    print(KnapsackGreedy(Ls, B, lambda x: x[0]))
    print(KnapsackGreedy(Ls, B, lambda x: -x[1]))
    print(KnapsackGreedy(Ls, B, lambda x: x[0]/x[1]))
    
    print(KnapsackPermutations(Ls, B))
    print(KnapsackCombinations(Ls, B))