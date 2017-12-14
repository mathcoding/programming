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
    for line in fh:
        row = line.replace('\n','').split('|')
        Rs.append((int(row[0]), int(row[1]), row[2], row[3], row[4]))
             
    return Rs

def CountGender(Ls):
    D = {}
    for l in Ls:
        D[l[2]] = 1+D.get(l[2], 0)
    return D

def CountOccupation(Ls):
    D = {}
    for l in Ls:
        D[l[3]] = 1+D.get(l[3], 0)
    return D

def CountAge(Ls):
    R = [0,0,0,0,0]
    for l in Ls:
        if l[1] < 18:
            R[0] += 1
        elif l[1] < 25:
            R[1] += 1
        elif l[1] < 40:
            R[2] += 1
        elif l[1] < 65:
            R[3] += 1
        else:
            R[4] += 1
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
    for line in fh:
        row = line.replace('\n','').split('|')
        Rs[int(row[0])] = row[1:]
    return Rs

def CountItem(Fs, i):
    t = 0
    for k in Ls:
        if Ls[k][i] == '1':
            t += 1
    return t

def CountYears(Fs):
    D = {}
    for k in Fs:
        date = Fs[k][1].split('-')
        if len(date) == 3: 
            year = int(date[2])
            D[year] = 1+D.get(year, 0)
    return D
    
# user id | item id | rating | timestamp
def ParseRatings(filename):
    fh = open(filename, 'r')
    Rs = []
    for line in fh:
        row = line.replace('\n','').split('\t')
        Rs.append(row)             
    return Rs

def CountField(Ls, v):
    D = {}
    for l in Ls:
        D[l[v]] = 1+D.get(l[v], 0)
    return D

def PrintTop(Ds, top=5):
    for key in sorted(Ds, key=Ds.get, reverse=True)[:top]:
        print(key, Ds[key])

def PrintTopFilm(Ds, top, Ts):
    for key in sorted(Ds, key=Ds.get, reverse=True)[:top]:
        print(Ts[int(key)][0], Ds[key])
    
#-----------------------------------------------
# MAIN function
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

    