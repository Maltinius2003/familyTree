from time import sleep
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineListItem
from kivy.app import App
from custom_widgets import CustomDateWidget
    
class AddFamilyTreeScreen(Screen):
    gender = StringProperty('u') # StringProperty nesserary to get the button state updated
    firstname = 'firstname'
    secondnames = ['secondname1', 'secondname2']
    lastname = 'lastname'
    birthdate = [0, 0, -1, False] # [day, month, year, bc?]
    deathdate = [0, 0, -1, False] # [day, month, year, bc?]

    def __init__(self, **kwargs):
        #self.gender = 'u'
        super().__init__(**kwargs)

    def screen_method(self):
        print('Hello from addfamilytree')

    def checkFirstName(self, instance):
        # Only allow alphanumeric characters and dashes, no dash-dash
        cleaned_text = ''
        previous_char = ''
        for i, ch in enumerate(instance.text):
            if i == 0 and ch == '-':
                continue
            if ch.isalpha() or ch == '-':
                if ch == '-' and previous_char == '-':
                    continue
                cleaned_text += ch
                previous_char = ch

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

    def checkDashAtEnd(self, instance):
        # Check if the last character is a dash or space, if so, throw an error
        if instance.text[-1:] != '':
            if instance.text[-1:] == '-':
                instance.error = True
                return False
            else:
                return True        

    def checkLastName(self, instance):
        self.checkSecondNames(instance)
    
    def removeSpaceAtEnd(self, text):
        if text[-1:] == ' ':
            return text[:-1]
        return text

    def setGender(self, gender):
        self.gender = gender
        #print(self.gender)

    def test(self):
        print('test')

    def back_to_menu(self):
        self.manager.current = 'menu'
        
    def save(self, instance):
        self.firstname = self.ids.firstname.text #remove Space unnecessary, no space allowed in first name
        self.secondnames = self.removeSpaceAtEnd(self.ids.secondnames.text)
        self.lastname = self.removeSpaceAtEnd(self.ids.lastname.text)

        self.birthdate[0] = self.ids.birthdate.day
        self.birthdate[1] = self.ids.birthdate.month
        self.birthdate[2] = self.ids.birthdate.year
        self.birthdate[3] = self.ids.birthdate.bc

        self.deathdate[0] = self.ids.deathdate.day
        self.deathdate[1] = self.ids.deathdate.month
        self.deathdate[2] = self.ids.deathdate.year
        self.deathdate[3] = self.ids.deathdate.bc

        print('Save button pressed')
        print(f'Firstname: {self.firstname}')
        print(f'Secondnames: {self.secondnames}')
        print(f'Lastname: {self.lastname}')
        print(f"Birthday: {self.birthdate[0]}.{self.birthdate[1]}.{self.birthdate[2]} {'BC' if self.birthdate[3] else 'AD'}")
        print(f"Deathday: {self.deathdate[0]}.{self.deathdate[1]}.{self.deathdate[2]} {'BC' if self.deathdate[3] else 'AD'}")

        

    



         
            


        

