def askIfcorrect(intake):
    choice = 'n'
    while choice.lower() != 'y' and choice.lower() != "":
        print('Correct?: ' + intake + ' ' + '(Y/n)')
        choice = input()
        if choice.lower() == "n":
            intake = input('Enter again: ')
        else:
            return intake
            
            