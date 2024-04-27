from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class AddFamilyTreeScreen(Screen):
    gender = StringProperty('u') # StringProperty nesserary to get the button state updated
    firstName = StringProperty('') 
    secondNames = StringProperty('')
    lastName = StringProperty('')


    def __init__(self, **kwargs):
        #self.gender = 'u'
        super().__init__(**kwargs)


    def screen_method(self):
        print('Hello from addfamilytree')

    def checkFirstName(self, instance):
        # Only allow alphanumeric characters and dashes
        cleaned_text = ''
        #print(instance.text)
        for ch in instance.text:
            if ch.isalpha() or ch == '-':
                cleaned_text += ch

        # Update the instance text with the cleaned text
        instance.text = cleaned_text

    def checkSecondNames(self, instance):
        # Only allow alphanumeric characters, dashes, and spaces, no space-space, dash-space, space-dash, or dash-dash
        cleaned_text = ''
        previous_char = ''
        for i, ch in enumerate(instance.text):
            if i == 0 and (ch == '-' or ch == ' '):
                continue
            if ch.isalpha() or ch == '-' or ch == ' ':
                if ch == ' ' and previous_char == '-':
                    continue
                if ch == '-' and previous_char == ' ':
                    continue
                if ch == '-' and previous_char == '-':
                    continue
                if ch == ' ' and previous_char == ' ':
                    continue
                cleaned_text += ch
                previous_char = ch

        # Update the instance text with the cleaned text
        instance.text = cleaned_text

    def checkDashOrSpaceAtEnd(self, instance):
        # Check if the last character is a dash or space, if so, throw an error
        if instance.text[-1:] == '-' or instance.text[-1:] == ' ':
            instance.error = True

    def checkLastName(self, instance):
        self.checkSecondNames(instance)

    def setGender(self, gender):
        self.gender = gender
        #print(self.gender)


         
            


        

