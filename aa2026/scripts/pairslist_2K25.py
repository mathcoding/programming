#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:41:01 2024

@author: gualandi
"""

from pairs import MakePair, First, Second, IsPair


# Versione della libreria
__version__ = '0.3.0'

# Lista delle funzioni che voglio esportare
__all__ = [
    'EmptyList', 'MakeList', 'Head', 'Tail', 'IsEmptyList', 'IsPairsList'
    ]

# Costruttore per il tipo di dati "PairsList"
def EmptyList():
    """ Restituisce una lista vuota """
    return None

def MakeList(x, Ls=EmptyList()):
    """ Costruttore di una lista.

           x : elemento da memorizzare nella lista
           Ls: coda della lista (deve essere una PairsList) """
    return MakePair(x, Ls)


# Selettori per il tipo di dati "PairsList"
def Head(Ls):
    """ Funzione che restituisce la testa della lista Ls """
    return First(Ls)

def Tail(Ls):
    """ Funzione che restituisce la coda della lista Ls """
    return Second(Ls)


# Predicato per il tipo di dato
def IsEmptyList(Ls):
    """ Predicato che controlla se la lista Ls è vuota """
    return Ls == EmptyList()

def IsPairsList(Ls):
    """ Predicato che controlla se Ls è una PairsList """
    if IsEmptyList(Ls):
        return True
    if IsPair(Ls):
        return IsPairsList(Tail(Ls))
    return False

# Costruisce una list di numeri interi positivi da "a" fino a "b"
def MakeIntRange(a, b):
    """ Restituisce la lista di numeri interi compresi tra a e b, con a <= b """
    # DA COMPLETARE
    return EmptyList()


def PrintList(Ls):
    print('TODO: completare')

# ------------------------------------------------------------------------------
# Aggiungere qui le soluzioni degli esercizi
# ------------------------------------------------------------------------------










