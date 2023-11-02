import helpMethods as hm

def askIfcorrect(intake, tabuChars=[]):
    choice = 'n'
    while choice.lower() != 'y' and choice.lower() != "":
        check = True
        if len(tabuChars) != 0:
            if not hm.stringTabuChars(intake, tabuChars):
                check = False

        if (check and hm.testSpaceDashLeadingClosing(intake) and hm.testSpaceDashTogether(intake)):
            print('Correct?: ' + intake + ' ' + '(Y/n)')
            choice = input()    
        else:
            print('Wrong format!')
        if choice.lower() == "n":
            intake = input('Enter again: ')
        else:
            return intake
            
            