import csv
import helpMethods as hm

with open('religions.csv') as f:
    reader = csv.reader(f)
    religions = list(reader)

longestLength = len(hm.getLongestListinList(religions))
orderdReligions = []
for i in range(longestLength-1): orderdReligions.append([])

for list in religions:
    for i in range(2, longestLength+1): #Gibt nur mindestens zweiteilige Spalten
        if len(list) == i:
            orderdReligions[i-2].append(list)

#print(orderdReligions)


original_list = [
    ['0', 'None'], ['1', 'Unknown'], ['2', 'Other'], ['3', 'Christianity'], ['4', 'Islam '],
    ['5', 'Judaism'], ['6', 'Hinduism'], ['7', 'Buddhism'], ['8', 'Sikhism'], ['9', 'BahÃ¡Ê¼Ã\xad Faith'],
    ['10', 'Shintoism'], ['11', 'Taoism'], ['12', 'Zoroastrianism'], ['13', 'Jainism'], ['14', 'Confucianism']
]

transposed_list = [[item[i] for item in original_list] for i in range(len(original_list[0]))]

print(transposed_list)

