import csv
import helpMethods as hm

def importReligions():
    with open('religions.csv') as f:
        reader = csv.reader(f)
        religions = list(reader)

    longestLength = len(hm.getLongestListinList(religions))
    orderdReligions = []
    for i in range(longestLength-1): orderdReligions.append([])

    for lst in religions:
        for i in range(2, longestLength+1): #Gibt nur mindestens zweiteilige Spalten
            if len(lst) == i:
                orderdReligions[i-2].append(lst)
    return orderdReligions



