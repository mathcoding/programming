# -*- coding: utf-8 -*-
"""
Soluzione Challenge Esercitazione 1: Conta cambi possibili di monete

@author: gualandi
"""

def Valore(tipo_di_moneta):
    if tipo_di_moneta == 1:
        return 1
    if tipo_di_moneta == 2:
        return 2
    elif tipo_di_moneta == 3:
        return 5
    elif tipo_di_moneta == 4:
        return 10
    elif tipo_di_moneta == 5:
        return 20
    elif tipo_di_moneta == 6:
        return 50
    
def CC(resto, tipo_di_moneta):
    if resto == 0:
        return 1
    elif resto < 0 or tipo_di_moneta == 0:
        return 0
    else:
        return CC(resto-Valore(tipo_di_moneta), tipo_di_moneta) + CC(resto, tipo_di_moneta-1)
            
def ContaCambi(centesimi):
    return CC(centesimi, 6)
    
print(ContaCambi(100))