# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:49:34 2017

@author: gualandi
"""

import matplotlib.pyplot as plt
import numpy as np
from time import time

# Rapido tutorial su numba:
# https://neurohackweek.github.io/cython-tutorial/04-numba/
from numba import jit

@jit
def JuliaSetRecIter(z, c, it, maxit=64):
    """ Funzione ricorsiva con processo iterativo """
    if it > maxit:
        return 0
    else:
        zp = z**2 + c
        if abs(zp) > 2:
            return it
        else:
            return JuliaSetRecIter(zp, c, it+1)

@jit
def JuliaSetForIter(z, c, it, maxit=64):
    """ Semplice processo iterativo """
    for it in range(maxit):
        z = z**2 + c
        if abs(z) > 2:
            return it        
    return 0
        
@jit
def JuliaSet(z, c=-0.413):
    return JuliaSetForIter(z, c, 0)


def PlotFractal(A):
    """ Stampa il frattale a video e lo salva su un file .pdf """
    plt.figure(figsize=(5,5))
    plt.tick_params(
        axis='both',       # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        left='off', labelleft='off',
        labelbottom='off') # labels along the bottom edge are off
    
    # SPECIFICARE IL NOME DEL VOSTRO FRATTALE
    plt.title("Frattale Flop, by Hans")
    # SPECIFICARE LA SUCCESSIONE USATA, E IL NUMERO MASSIMO DI ITERAZIONI
    plt.xlabel('$z_{k+1}=z_k^2 - 0.423$\naltre info...')
    
    plt.imshow(A, extent=(-scale*n, scale*n, -scale*n, scale*n), animated=False, cmap='jet')
    # SALVARE L'IMMAGINE SU UN PDF CON UNA PRECISIONE DPI=300
    plt.savefig("prova.pdf", dpi=300)
    
    plt.show()

#-----------------------------------------------
# MAIN function
#-----------------------------------------------
if __name__ == "__main__":     
    n = 500
    c = -0.423
    scale = 0.004

    data = [scale*i for i in range(-n,n)]

    ## Basic time profiling for measuring the effect of the @jit compiler    
    start = time()

    # Build the matrix giving the fractal
    A = np.matrix([[JuliaSet(complex(i, j), c) for i in data] for j in data])
    
    ## Basic time profiling for measuring the effect of the @jit compiler
    end = time()
    print('run time: {}'.format(end-start))
    
    # Plot the matrix
    PlotFractal(A)