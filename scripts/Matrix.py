# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:14:24 2017

@author: gualandi
"""

class Matrix(object):
    def __init__(self, nrows, ncols, a=0):
        if type(nrows) != int:
            raise TypeError("Pistola! Il numero di righe deve essere un intero")
        if type(ncols) != int:
            raise TypeError("Pistola! Il numero di colonne deve essere un intero")
            
        self.n = nrows
        self.m = ncols
        self.A = [[a for _ in range(ncols)] for _ in range(nrows)]
    
    def __str__(self):
        s = '['
        for i, row in enumerate(self.A):
            s += '['
            for j,e in enumerate(row):                
                s += str(e)
                if j < self.m-1:
                    s += ', '
                else:
                    s += ']'            
            if i < self.n-1:
                s += ',\n '
            else:
                s += ']'            
        return s
    
    def __add__(self, B):
        if not isinstance(B, Matrix):
            raise TypeError("Giovine matricola, puoi solo sommare due matrici..")
        if B.n != self.n or B.m != self.m:
            raise RuntimeError("Giovine matricola, le due matrici devono avere la stessa dimensione")
            
        return list(map(lambda rowb, rowa: list(map(lambda a,b: a+b, rowb, rowa)), B.A, self.A))
            
    def SetValue(self, i, j, value):
        self.A[i][j] = value

    def GetValue(self, i, j, value):
        return self.A[i][j]
    
    
    
#-----------------------------------------------
# MAIN function
#-----------------------------------------------
if __name__ == "__main__":    
    try:
        B = Matrix('3', '1')
    except TypeError as e:
        print('Presa prima eccezzione:', e)

    A = Matrix(2,3)
    print(type(A))
    print(A)
    A.SetValue(1, 2, 4)
    print(A)
  
    B = Matrix(2,3,5)
    print(A+B)          
     
    
    