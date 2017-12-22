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
        
        
def KR(Left, Br):
    if Left == [] or Br == 0:
        return (0, ())
    nextItem = Left[0]
    if nextItem[1] > Br:
        # Right branch
        return KR(Left[1:], Br)
    # Explore left branch: take the item
    leftVal, leftSol = KR(Left[1:], Br-nextItem[1])
    leftVal += nextItem[0] # Update profit
    
    # Explore right branch: leave out the item
    rightVal, rightSol = KR(Left[1:], Br)
    
    # Select and return the best solution
    if leftVal > rightVal:
        return (leftVal, leftSol + (nextItem,))
    else:
        return (rightVal, rightSol)    
    
    
def DP(Left, Br, memo = {}):
    # Similar to memoization
    if (len(Left), Br) in memo:
        return memo[(len(Left), Br)]
    else:
        if Left == [] or Br == 0:
            return (0, ())
        nextItem = Left[0]
        if nextItem[1] > Br:
            # Right branch
            result = DP(Left[1:], Br, memo)
        else:
            # Explore left branch: take the item
            leftVal, leftSol = DP(Left[1:], Br-nextItem[1], memo)
            leftVal += nextItem[0] # Update profit
            
            # Explore right branch: leave out the item
            rightVal, rightSol = DP(Left[1:], Br, memo)
            
            # Select and return the best solution
            if leftVal > rightVal:
                result = (leftVal, leftSol + (nextItem,))
            else:
                result = (rightVal, rightSol)    

        memo[(len(Left), Br)] = result
        return result
    
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
    
    from random import randint
    Is = [(randint(1,100), randint(5, 25)) for _ in range(30)]
    B = 95
    
    import cProfile
    cProfile.run('KR(Is,B)')
    cProfile.run('DP(Is,B)')
    #print(KR(Ls, B))
    #print(DP(Ls, B))