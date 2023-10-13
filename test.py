import csv
import helpMethods as hm
with open('religions.csv') as f:
    reader = csv.reader(f)
    religions = list(reader)
#print(religions)

longestLength = len(hm.getLongestListinList(religions))
orderdReligions = []
for i in range(longestLength-1): orderdReligions.append([])

for list in religions:
    for i in range(2, longestLength+1): #Gibt nur zweiteilige Spalten
        if len(list) == i:
            orderdReligions[i-2].append(list)



print(orderdReligions)