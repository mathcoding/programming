# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:47:43 2017

@author: gualandi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:45:33 2017

@author: gualandi
"""

# Parse a file where for each row we have:
#  user id | age | gender | occupation | zip code
#  1|24|M|technician|85711
def ParseUsers(filename):
    fh = open(filename, 'r', encoding="utf-8")
    Rs = []
    # DA COMPLETARE             
    return Rs

def CountGender(Ls):
    D = {}
    # DA COMPLETARE             
    return D

def CountOccupation(Ls):
    D = {}
    # DA COMPLETARE             
    return D

def CountAge(Ls):
    R = [0,0,0,0,0]
    # DA COMPLETARE             
    return R
            
# Info for each film:
#  movie id | movie title | release date | video release date |
#          IMDb URL | unknown | Action | Adventure | Animation |
#          Children's | Comedy | Crime | Documentary | Drama | Fantasy |
#          Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
#          Thriller | War | Western |
def ParseFilm(filename):
    fh = open(filename, 'r')
    Rs = {}
    # DA COMPLETARE             
    return Rs

def CountItem(Fs, i):
    t = 0
    # DA COMPLETARE             
    return t

def CountYears(Fs):
    D = {}
    # DA COMPLETARE             
    return D
    
# user id | item id | rating | timestamp
def ParseRatings(filename):
    fh = open(filename, 'r')
    Rs = []
    # DA COMPLETARE             
    return Rs

def CountField(Ls, v):
    D = {}
    # DA COMPLETARE             
    return D

def PrintTop(Ds, top=5):
    for key in sorted(Ds, key=Ds.get, reverse=True)[:top]:
        print(key, Ds[key])

def PrintTopFilm(Ds, top, Ts):
    # DA COMPLETARE             
    pass
    
#-----------------------------------------------
# MAIN function: da usare in fase di test
#-----------------------------------------------
if __name__ == "__main__":    
    Ls = ParseUsers('../data/u.user')
    
    print(CountGender(Ls))
    Os = CountOccupation(Ls)
    PrintTop(Os)
    print(CountAge(Ls))
    
    Ls = ParseFilm('../data/u.item')
    PrintTop(Ls)
    print(CountItem(Ls, 20))  # 251
    Fs = CountYears(Ls)
    PrintTop(Fs)
    
    
    Rs = ParseRatings('../data/u1.base')
    print()
    PrintTop(CountField(Rs, 2))
    print()
    PrintTop(CountField(Rs, 0))
    print()
    PrintTop(CountField(Rs, 1))
    print()
    PrintTopFilm(CountField(Rs, 1), 10, Ls)