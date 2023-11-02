def askIfcorrect(intake, forcealpha=False): #Nur alphabetische Zeichen, auch keine Leerzeichen erlaubt
    choice = 'n'
    while choice.lower() != 'y' and choice.lower() != "":
        if (forcealpha and intake.isalpha()) or not forcealpha:
            print('Correct?: ' + intake + ' ' + '(Y/n)')
            choice = input()    
        else:
            print('Spaces or numbers are not allowed ')
        if choice.lower() == "n":
            intake = input('Enter again: ')
        else:
            return intake
            
            