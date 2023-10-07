def name_to_name_parts(nameStr):
    name_parts = nameStr.split("-")
    return name_parts

def strList_to_str(strList, gap='-'):
    complete = gap.join(strList)
    return complete

def name_to_str(self):
    namePartListStr = []
    for np in self.nameComplete:
        namePartListStr.append(np.part)
    return strList_to_str(namePartListStr)

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
    print("Von welchem Typ ist der Name: " + hm.namePartsToString(neu) + "?")
    if neu.nameComplete.size() > 1:
        print("0 Ergibt nur in Einzelteilen Sinn")
    print("1 Unbekannt")
    print("2 Durch Geburt angenommen")
    print("3 Durch Heirat angenommen")
    print("4 Durch Adoption angenommen")
    
    #in = input()
    
    ###

    return neu

