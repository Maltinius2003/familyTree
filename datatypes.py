class Religion:
    def __init__(self):
        self.main = 0
        self.otherMain = ""
        self.mainConfession = 0
        self.otherMainConfession = ""
        self.underConfession = 0
        self.otherUnderConfession = ""
        self.joinDate = ""
        self.leaveDate = ""

class Relation:
    def __init__(self):
        self.partner = None
        self.marriage = False
        self.marriageType = 0
        self.churchMarriageType = None
        self.startDate = ""
        self.endDate = ""
        self.legallyBinding = 0
        self.breaks = []

    class RelationBreak:
        def __init__(self):
            self.startDate = ""
            self.endDate = ""

class Gender:
    def __init__(self):
        self.gen = ''
        self.type = 0
        self.joinDate = ""
        self.leaveDate = ""

class Name:
    def __init__(self):
        self.nameComplete = []
        self.type = 0
        self.origin = 1
        self.namedAfter = []
        self.otherNamedAfter = ""
        self.givenDate = ""
        self.takenDate = ""

    class NamePart:
        def __init__(self, part):
            self.part = part
            self.origin = 1
            self.namedAfter = []

class Degree:
    def __init__(self):
        self.title = ""
        self.subject = ""
        self.acquisitionDate = ""