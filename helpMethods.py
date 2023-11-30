import csv

def string_to_parts(nameStr, sepSymbolsList):
    parts = []
    sepSymbols = []
    currentPart = ""

    for symbol in sepSymbolsList:
        nameStr = nameStr.strip(symbol)

    for char in nameStr:
        if char in sepSymbolsList:
            if currentPart:
                parts.append(currentPart)
                currentPart = ""
            sepSymbols.append(char)
        else:
            currentPart += char

    if currentPart:
        parts.append(currentPart)

    return parts, sepSymbols

def strList_to_str(strList):
    complete = ''.join(strList)
    return complete

def name_to_str(self):
    namePartListStr = []
    for i in range(len(self.nameComplete)):
        namePartListStr.append(self.nameComplete[i].part)
        if i<len(self.nameComplete)-1: namePartListStr.append(self.nameSepSymbols[i])
    return strList_to_str(namePartListStr)

def getLongestListinList(listoflists):
    max = 0
    pos = None
    for i, l in enumerate(listoflists):
        if len(l) > max:
            max = len(l)
            pos = i
    return listoflists[pos]
    
def stringTabuChars(s, chars=[]):
    for t in chars:
        if t in s:
            return False
    return True

#test if space or - is leading or closing
def testSpaceDashLeadingClosing(name):
    if name[0] == ' ' or name[0] == '-':
        return False
    if name[-1] == ' ' or name[-1] == '-':
        return False
    return True

#test if space or - together   
def testSpaceDashTogether(s):
    for i in range(len(s)-1):
        if s[i] == ' ' and s[i+1] == ' ':
            return False
        if s[i] == '-' and s[i+1] == '-':
            return False
        if s[i] == ' ' and s[i+1] == '-':
            return False
        if s[i] == '-' and s[i+1] == ' ':
            return False
    return True

def transpose_list(input_list):
    transposed_list = []

    # Bestimme die Anzahl der Spalten
    num_columns = len(input_list[0])

    # Iteriere über die Spalten
    for i in range(num_columns):
        # Erstelle eine Liste für die aktuelle Spalte
        current_column = []

        # Iteriere über die Zeilen und füge das i-te Element zur aktuellen Spalte hinzu
        for row in input_list:
            current_column.append(row[i])

        # Füge die aktuelle Spalte zur transponierten Liste hinzu
        transposed_list.append(current_column)

    return transposed_list

### Noch nicht überarbeitet
def askFirstNameOrigin(self):
    print("Welchen Ursprung hat der Name " + name_to_str(self) + "?")
    if len(self.nameComplete) > 1:
        print("0 Ergibt nur in Einzelteilen Sinn")
    print("1 Kein besonderer Bezug")
    print("2 Nach Verwandtem benannt")
    print("3 Nach Paten (verwandt) benannt")
    print("4 Nach Paten (nicht verwandt) benannt")
    print("5 Nach Heiligem benannt")
    origin = int(input())
    self.origin = origin
    if len(self.nameComplete) > 1:
        for i in range(len(self.nameComplete)):
            print("Welchen Ursprung hat der Namensteil " + self.nameComplete[i].part + "?")
            print("1 Kein besonderer Bezug")
            print("2 Nach Verwandtem benannt")
            print("3 Nach Paten (verwandt) benannt")
            print("4 Nach Paten (nicht verwandt) benannt")
            print("5 Nach Heiligem benannt")
            origin = int(input())
            self.nameComplete[i].origin = origin
    return self

def askLastNameType(name):
    neu = name
    print("Von welchem Typ ist der Name: " + name_to_str(neu) + "?")
    if neu.nameComplete.size() > 1:
        print("0 Ergibt nur in Einzelteilen Sinn")
    print("1 Unbekannt")
    print("2 Durch Geburt angenommen")
    print("3 Durch Heirat angenommen")
    print("4 Durch Adoption angenommen")
    
    #in = input()
    
    ###

    return neu

