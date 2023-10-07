from enum import Enum

import dict
import person as p
import datatypes as dt
import helpMethods as hm

persons = []

class Language(Enum):
    GERMAN = "de"
    ENGLISH = "en"

d = dict()
current_language = Language.GERMAN
current_language = Language.ENGLISH

def main():
    createPerson()
    for n in persons[0].getFirstNames():
        print(hm.name_to_str(n))

def createPerson():
    p1 = p.Person()

    in1 = input('Amtlicher Vorname: ')
    p1.addName(0, in1, 1)
    choice = 'n'
    while choice.lower() != 'j' and choice.lower() != "":
        print('Name korrekt?: ' + p1.getLastAddedFirstName() + ' ' + '(J/n)')
        choice = input()
        if choice.lower() == "n":
            p1.delLastAddedName(0)
            in1 = input('Name erneut eingeben: ')
            p1.addName(0, in1, 1)
        else:
            break

    

    persons.append(p1)

if __name__ == "__main__":
    main()