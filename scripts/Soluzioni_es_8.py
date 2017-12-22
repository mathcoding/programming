# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 09:38:02 2017

@author: gualandi
"""

# Parse a file where for each row we have:
#  user id | age | gender | occupation | zip code
#  1|24|M|technician|85711
def ParseUsers(filename):
    fh = open(filename, 'r', encoding="utf-8")
    Rs = {}
    for line in fh:
        row = line.replace('\n','').split('|')
        Rs[int(row[0])] = (int(row[1]), row[2], row[3], row[4])
             
    return Rs

# user id | item id | rating | timestamp
def ParseRatings(filename):
    fh = open(filename, 'r')
    Rs = {}
    for line in fh:
        row = line.replace('\n','').split('\t')
        user_id, item_id = int(row[0]), int(row[1])
        Rs[(user_id, item_id)] = int(row[2])
    return Rs

def PrintTop(Ds, top=5):
    for key in sorted(Ds, key=Ds.get, reverse=True)[:top]:
        print(key, Ds[key])

# Support: compute average of a list of values
def Mean(Ls):
    return sum(Ls)/len(Ls)

# In alternativa si può usare la libreria "statistics"
# Link: https://docs.python.org/3/library/statistics.html
# ===> from statistics import mean
    
# Esercizio 8.2: compute average of all rating
def ComputeAverage(Ls):
    return Mean(Ls.values())

# Esercizio 8.3    
def ComputeItemAverage(Ls):
    Is = {}
    for key in Ls:
        user_id, item_id = key  # Unfolding
        Is[item_id] = Is.get(item_id, []) + [Ls[key]]
        
    for item in Is:
        Is[item] = Mean(Is[item])#, len(Is[item])
    
    return Is

# Esercizio 8.4
def ComputeUserAverage(Ls):
    Is = {}
    for key in Ls:
        user_id, item_id = key  # Unfolding
        Is[user_id] = Is.get(user_id, []) + [Ls[key]]
        
    for key in Is:
        Is[key] = Mean(Is[key])
    
    return Is

# Esercizio 8.5
def ComputeUserTypeAverage(Ls, Us):
    Is = {}
    for key in Ls:
        user_id, item_id = key  # Unfolding
        type_id = Us.get(user_id, 'none')[2]
        Is[type_id] = Is.get(type_id, []) + [Ls[key]]
        
    for key in Is:
        Is[key] = Mean(Is[key])
    
    return Is

# Esercizio 8.6
def Round(x):
    return round(x, 0)

def PredictAvg(TrainingSet, TestSet):
    avg = ComputeAverage(TrainingSet)    
    Ps = {}
    for key in TestSet:
        Ps[key] = Round(avg)
    return Ps

# Esercizio 8.7
from math import sqrt
def RMSE(Yb, Y):
    return sqrt(Mean(list(map(lambda k: (Yb[k]-Y[k])**2, Yb))))

def nRMSE(Yb, Y):
    return RMSE(Yb,Y)/4

def RMSE2(Yb, Y):   
    # Riusare metodi da libreria di Machine Learning
    # Link: http://scikit-learn.org/stable/
    from sklearn.metrics import mean_squared_error
    A = list(map(lambda k: Y[k], sorted(Y)))
    B = list(map(lambda k: Yb[k], sorted(Y)))
    return sqrt(mean_squared_error(A, B))
    
def R2_Score(Yb, Y):   
    # Riusare metodi da libreria di Machine Learning
    # Link: http://scikit-learn.org/stable/
    from sklearn.metrics import r2_score
    A = list(map(lambda k: Y[k], sorted(Y)))
    B = list(map(lambda k: Yb[k], sorted(Y)))
    return r2_score(A, B)

    
def MAE(Yb, Y):   
    # Riusare metodi da libreria di Machine Learning
    # Link: http://scikit-learn.org/stable/    
    from sklearn.metrics import mean_absolute_error
    A = list(map(lambda k: Y[k], sorted(Y)))
    B = list(map(lambda k: Yb[k], sorted(Y)))
    return mean_absolute_error(A, B)

# Esercizio 8.9
def PredictAvgItem(TrainingSet, TestSet):
    avg = ComputeAverage(TrainingSet)
    As = ComputeItemAverage(TrainingSet)    
    Ps = {}
    for key in TestSet:
        _, item_id = key  # Unfolding
        Ps[key] = Round(As.get(item_id, avg))
    return Ps

def PredictAvgUser(TrainingSet, TestSet):
    avg = ComputeAverage(TrainingSet)
    As = ComputeUserAverage(TrainingSet)    
    Ps = {}
    for key in TestSet:
        user_id, _ = key  # Unfolding
        Ps[key] = Round(As.get(user_id, avg))
    return Ps

def PredictAvgCategory(TrainingSet, TestSet, Users):
    avg = ComputeAverage(TrainingSet)
    As = ComputeUserTypeAverage(TrainingSet, Users) 
    Ps = {}
    for key in TestSet:
        user_id, _ = key  # Unfolding
        type_id = Users.get(user_id, 'none')[2]
        Ps[key] = Round(As.get(type_id, avg))
    return Ps

def SingleTest(Users, n, Metric=RMSE):
    TrainingSet = ParseRatings('../data/u{}.base'.format(n))
    TestSet = ParseRatings('../data/u{}.test'.format(n))
    
    print('Avg globale:  ', Metric(PredictAvg(TrainingSet, TestSet), TestSet))
    print('Avg film:     ', Metric(PredictAvgItem(TrainingSet, TestSet), TestSet))
    print('Avg utente:   ', Metric(PredictAvgUser(TrainingSet, TestSet), TestSet))
    print('Avg cat user: ', Metric(PredictAvgCategory(TrainingSet, TestSet, Users), TestSet))
    print('Avg file/user:', Metric(PredictAvgAvg(TrainingSet, TestSet), TestSet))
    
    
def PredictAvgAvg(TrainingSet, TestSet, Users):
    avg = ComputeAverage(TrainingSet)
    Is = ComputeItemAverage(TrainingSet)    
    Us = ComputeUserAverage(TrainingSet) 
    As = ComputeUserTypeAverage(TrainingSet, Users) 
    Ps = {}
    for key in TestSet:
        user_id, item_id = key
        avg1 = Is.get(item_id, avg)
        avg2 = Us.get(user_id, avg)
        Ps[key] = Round((avg1+avg2)/2)
    return Ps


#-----------------------------------------------
# MAIN function
#-----------------------------------------------
if __name__ == "__main__":    
    Users = ParseUsers('../data/u.user')
    if False:
        TrainingSet = ParseRatings('../data/u1.base')
        TestSet = ParseRatings('../data/u1.test')
        print(len(TrainingSet), len(TestSet))
        
        print('Compute Global Average {}'.format(ComputeAverage(TrainingSet)))
        Is = ComputeItemAverage(TrainingSet)
        PrintTop(Is)
        
        Us = ComputeUserAverage(TrainingSet)
        PrintTop(Us)
    
        Ts = ComputeUserTypeAverage(TrainingSet, Users)
        PrintTop(Ts, top=100)
        
        # Naive prediction
        Pbar = PredictAvg(TrainingSet, TestSet)
        
        # Esercizio 8.8
        print(RMSE(Pbar, TestSet))
        # Esercizio 8.9
        print(RMSE(PredictAvgItem(TrainingSet, TestSet), TestSet))
        print(RMSE(PredictAvgUser(TrainingSet, TestSet), TestSet))
        print(RMSE(PredictAvgCategory(TrainingSet, TestSet, Users), TestSet))
        print(RMSE(PredictAvgAvg(TrainingSet, TestSet), TestSet))
    else:
        for n in range(1,6):
            print('Test set: training=u{}.base, test=u{}.test:'.format(n, n))
            SingleTest(Users, n, RMSE)