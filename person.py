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
        return self.getAllFirstNames()

    def addName(self, firstSecondFamily, n, type=0, origin=1):
        if n != '':
            nameParts, sepSymbols = hm.name_to_name_parts(n)
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
    



    def isAdoptedFather(self):
        return self.adoptedFather

    def setAdoptedFather(self, adoptedFather):
        self.adoptedFather = adoptedFather

    def isAdoptedMother(self):
        return self.adoptedMother

    def setAdoptedMother(self, adoptedMother):
        self.adoptedMother = adoptedMother

    def getFirstNames(self):
        return self.firstNames

    def setFirstNames(self, firstNames):
        self.firstNames = firstNames

    def getSecondNames(self):
        return self.secondNames

    def setSecondNames(self, secondNames):
        self.secondNames = secondNames

    def getFamilyNames(self):
        return self.familyNames

    def setFamilyNames(self, familyNames):
        self.familyNames = familyNames

    def getAcademicDegrees(self):
        return self.academicDegrees

    def setAcademicDegrees(self, academicDegrees):
        self.academicDegrees = academicDegrees

    def getRelations(self):
        return self.relations

    def setRelations(self, relations):
        self.relations = relations

    def getGenders(self):
        return self.genders

    def setGenders(self, genders):
        self.genders = genders

    def getBirthDate(self):
        return self.birthDate

    def setBirthDate(self, birthDate):
        self.birthDate = birthDate

    def getDeathDate(self):
        return self.deathDate
    
    def setDeathDate(self, deathDate):
        self.deathDate = deathDate

    def getDeathReason(self):
        return self.deathReason

    def setDeathReason(self, deathReason):
        self.deathReason = deathReason

    def getReligions(self):
        return self.religions

    def setReligions(self, religions):
        self.religions = religions

    def getMother(self):
        return self.mother

    def setMother(self, mother):
        self.mother = mother

    def getFather(self):
        return self.father

    def setFather(self, father):
        self.father = father

    def getChildren(self):
        return self.children

    def setChildren(self, children):
        self.children = children

    def getGodfathers1(self):
        return self.godfathers1

    def setGodfathers1(self, godfathers1):
        self.godfathers1 = godfathers1

    def getGodfathers2(self):
        return self.godfathers2

    def setGodfathers2(self, godfathers2):
        self.godfathers2 = godfathers2

    def getGodchilds(self):
        return self.godchilds

    def setGodchilds(self, godchilds):
        self.godchilds = godchilds