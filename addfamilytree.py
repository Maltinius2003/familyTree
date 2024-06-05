from time import sleep
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineListItem
from kivy.app import App
from custom_widgets import CustomDateWidget
from kivy.metrics import dp
from kivy.core.window import Window

import person
    
class AddFamilyTreeScreen(Screen):
    gender = 0 # 0 = unknown
    firstname = 'firstname'
    secondnames = ['secondname1', 'secondname2']
    lastnames = 'lastname'
    birthdate = [None, None, None, None, None, None, None, None, None] # [day, month, year, bc?, hour, minute, second, microsecond, time_zone]
    deathdate = [None, None, None, None, None, None, None, None, None] # [day, month, year, bc?, hour, minute, second, microsecond, time_zone]

    def __init__(self, **kwargs):
        #self.gender = 'u'
        super().__init__(**kwargs)
        Window.bind(on_resize=self.on_window_resized)
        #Window.bind(on_pre_resize=self.on_pre_window_resize)
        
    def on_window_resized(self, window, width, height):
        # Get the size of the parent layout
        parent_width = width
        parent_width_dp = dp(parent_width/2)
        print(f"Parent layout width: {parent_width} pixels, {parent_width_dp} dp")

        # Access the segmented control and set its width
        self.ids.segment_control.ids.segment_panel.width = parent_width_dp

    def on_access(self): # called when screen is accessed
        self.on_window_resized(Window, Window.width, Window.height)

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

    def set_gender(self, segment_control, segment_item):
        if segment_item == self.ids.gender_u:
            self.gender = 0
        elif segment_item == self.ids.gender_m:
            self.gender = 1
        elif segment_item == self.ids.gender_f:
            self.gender = 2
        elif segment_item == self.ids.gender_d:
            self.gender = 3 
        #self.gender = gender_num
        #print(self.gender)

    def test(self):
        print('test')

    def back_to_menu(self):
        self.manager.current = 'menu'
        
    def save(self, instance):

        self.firstname = self.ids.firstname.text #remove Space unnecessary, no space allowed in first name
        self.secondnames = self.removeSpaceAtEnd(self.ids.secondnames.text)
        self.lastnames = self.removeSpaceAtEnd(self.ids.lastname.text)

        self.birthdate[0] = self.ids.birthdate.day
        self.birthdate[1] = self.ids.birthdate.month
        self.birthdate[2] = self.ids.birthdate.year
        self.birthdate[3] = self.ids.birthdate.bc

        self.deathdate[0] = self.ids.deathdate.day
        self.deathdate[1] = self.ids.deathdate.month
        self.deathdate[2] = self.ids.deathdate.year
        self.deathdate[3] = self.ids.deathdate.bc

        #print('Save button pressed')
        #print(f'Firstname: {self.firstname}')
        #print(f'Secondnames: {self.secondnames}')
        #print(f'Lastname: {self.lastnames}')
        #print(f"Birthday: {self.birthdate[0]}.{self.birthdate[1]}.{self.birthdate[2]} {'BC' if self.birthdate[3] else 'AD'}")
        #print(f"Deathday: {self.deathdate[0]}.{self.deathdate[1]}.{self.deathdate[2]} {'BC' if self.deathdate[3] else 'AD'}")

        # Create a new person object
        p = person.Person()
        
        p.add_gender(self.gender)
        p.add_firstname(self.firstname)
        p.add_secondnames(self.secondnames)
        p.add_lastnames(self.lastnames)
        p.add_birth_date(self.birthdate)
        p.add_death_date(self.deathdate)
        


        p.print_everything()

        

    



         
            


        

