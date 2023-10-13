import person as p
import datatypes as dt
import helpMethods as hm
import consoleQuestions as cQ

persons = []

def main():
    createPerson()
    for n in persons[0].getFirstNames():
        print(hm.name_to_str(n))

def createPerson():
    p1 = p.Person()

    firstName = input('Official First Name: ')
    firstName = cQ.askIfcorrect(firstName)
    p1.addName(0, firstName, 1)

    familyName = input('Family Name: ')
    familyName = cQ.askIfcorrect(familyName)
    p1.addName(2, familyName)    

    persons.append(p1)

if __name__ == "__main__":
    main()