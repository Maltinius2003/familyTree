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
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_resize=self.on_window_resized)
        
        self.gender = 0 # 0 = unknown
        self.firstname = 'firstname'
        self.secondnames = ['secondname1', 'secondname2']
        self.lastnames = 'lastname'
        self.birthdate = [None, None, None, None, None, None, None, None, None] # [day, month, year, bc?, hour, minute, second, microsecond, time_zone]
        self.deathdate = [None, None, None, None, None, None, None, None, None] # [day, month, year, bc?, hour, minute, second, microsecond, time_zone]
        self.deathdate_unknown = False
        
    def on_window_resized(self, window, width, height):
        # Get the size of the parent layout
        parent_width = width
        parent_width_dp = dp(parent_width/2)
        #print(f"Parent layout width: {parent_width} pixels, {parent_width_dp} dp")

        # Access the segmented control and set its width
        self.ids.segment_control.ids.segment_panel.width = parent_width_dp

    def on_access(self): # called when screen is accessed, self defined called wenn buttons is pressed
        self.on_window_resized(Window, Window.width, Window.height)

    def on_opacity(self, instance, value):
        print("testsdfsdfsdf")

    def screen_method(self):
        print('Hello from addfamilytree')

    def test(self):
        print('test')

    def set_gender(self, segment_control, segment_item):
        if segment_item == self.ids.gender_u:
            self.gender = 0
        elif segment_item == self.ids.gender_m:
            self.gender = 1
        elif segment_item == self.ids.gender_f:
            self.gender = 2
        elif segment_item == self.ids.gender_d:
            self.gender = 3 
        #print(self.gender)

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

    def check_dates(self):
        # AD = False, BC = True

        # Check if the birthyear is greater than the deathyear
        if self.birthdate[2] is not None and self.deathdate[2] is not None:
            # Check if the birthyear is greater than the deathyear, anno domini
            if self.birthdate[2] > self.deathdate[2] and not self.birthdate[3] and not self.deathdate[3]:
                return False
            # Check if the birthyear is greater than the deathyear, before christ
            if self.birthdate[2] < self.deathdate[2] and self.birthdate[3] and self.deathdate[3]:
                return False
            # Check if the birthmonth is greater than the deathmonth, if the birthyear is the same as the deathyear
            if self.birthdate[1] is not None and self.deathdate[1] is not None and self.birthdate[2] == self.deathdate[2]:
                if self.birthdate[1] > self.deathdate[1]:
                    return False
                # Check if the birthday is greater than the deathday, if the birthyear and birthmonth are the same as the deathyear and deathmonth
                if self.birthdate[0] is not None and self.deathdate[0] is not None and self.birthdate[1] == self.deathdate[1]:
                    if self.birthdate[0] > self.deathdate[0]:
                        return False
        # birthdate ad and deathdate bc
            if not self.birthdate[3] and self.deathdate[3]:
                return False
        # birthdate bc and deathdate ad, always true  
        
        return True
    
    def set_deathdate_unknown(self, active):
        
        if active:
            self.ids.deathdate.set_day(0)
            self.ids.deathdate.month = None
            self.ids.deathdate.year = None
            self.ids.deathdate.bc = False

            self.deathdate_unknown = True
        else:
            self.deathdate_unknown = False

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

        if self.check_dates():
            # Create a new person object
            p = person.Person()
            
            p.add_gender(self.gender)
            p.add_firstname(self.firstname)
            p.add_secondnames(self.secondnames)
            p.add_lastnames(self.lastnames)
            p.add_birth_date(self.birthdate)
            p.add_death_date(self.deathdate)
            p.add_deathdate_unknown(self.deathdate_unknown)
            


            p.print_everything()

            # Add the person to the family tree
            App.get_running_app().add_person(p)
        
        else:
            print('Error: Birthdate is greater than deathdate')

        

    



         
            


        

