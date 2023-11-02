import helpMethods as hm
import datatypes as dt

class Person:
    def __init__(self):
        self.adoptedFather = False
        self.adoptedMother = False
        self.firstNames = []
        self.secondNames = []
        self.familyNames = []
        self.academicDegrees = []
        self.relations = []
        self.genders = []
        self.birthDate = ""
        self.deathDate = ""
        self.deathReason = ""
        self.religions = []
        self.mother = None
        self.father = None
        self.children = []
        self.godfathers1 = []
        self.godfathers2 = []
        self.godchilds = []

    def __str__(self):
        all_names = []

        for name in self.firstNames:
            all_names.append(hm.name_to_str(name))

        for name in self.secondNames:
            all_names.append(hm.name_to_str(name))

        for name in self.familyNames:
            all_names.append(hm.name_to_str(name))

        return ', '.join(all_names)

    def delLastAddedName(self, firstSecondFamily):
        if firstSecondFamily == 0:
            self.firstNames.pop()
        elif firstSecondFamily == 1:
            self.secondNames.pop()
        elif firstSecondFamily == 2:
            self.familyNames.pop()

    def getFirstNames(self):
        return self.firstNames
    
    def getOffFirstName(self):
        for name in self.firstNames:
            if name.type == 1 and name.takenDate == "":
                return hm.strList_to_str(name)
        return "-1"

    def getLastAddedFirstName(self):
        if len(self.firstNames) != 0:
            return hm.name_to_str(self.firstNames[-1])
        return ""
    
    def addName(self, firstSecondFamily, n, type=0, origin=1):
        nameParts, sepSymbols = hm.string_to_parts(n, [' ', '-'])
        complete = dt.Name()
        for namePart in nameParts:
            complete.nameComplete.append(dt.Name.NamePart(namePart))
        complete.nameSepSymbols = sepSymbols
        complete.type = type
        complete.origin = origin
        if firstSecondFamily == 0:
            self.firstNames.append(complete)
        elif firstSecondFamily == 1:
            self.secondNames.append(complete)
        elif firstSecondFamily == 2:
            self.familyNames.append(complete)

    def addNames(self, firstSecondFamily, n, type=None, origin=None):
        names, sepSymbols = hm.string_to_parts(n, [' '])

        if isinstance(firstSecondFamily, int):
            firstSecondFamily = [firstSecondFamily] * len(names)

        if type == None:
            type = [0] * len(names)
        if origin == None:
            origin = [1] * len(names)
        for i in range(len(firstSecondFamily)):
            self.addName(firstSecondFamily[i], names[i], type[i], origin[i])

    def delLastAddedName(self, firstSecondFamily):
        if firstSecondFamily == 0:
            self.firstNames.pop()
        elif firstSecondFamily == 1:
            self.secondNames.pop()
        elif firstSecondFamily == 2:
            self.familyNames.pop()

    def getFirstNames(self):
        return self.firstNames
    
    def getOffFirstName(self):
        for name in self.firstNames:
            if name.type == 1 and name.takenDate == "":
                return hm.strList_to_str(name)
        return "-1"

    def getLastAddedFirstName(self):
        if len(self.firstNames) != 0:
            return hm.name_to_str(self.firstNames[-1])
        return ""