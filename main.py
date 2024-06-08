from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp

import os
import jsonpickle
import json
from json import JSONEncoder

import showfamilytree
import menu
import addfamilytree
import settings

Window.size = (400, 600)

# Hierarchie:
#   familyTreeApp (App)
#   |- MyScreens (ScreenManager)
#      |- ShowFamilyTreeScreen (Screen)
#      |- MenuScreen (Screen)
#      |- AddFamilyTreeScreen (Screen)
#      |- Settings (Screen)

class MyScreens(ScreenManager):
    def screen_manager_method(self):
        print('Hello from screen manager')

class familyTreeApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Family Tree App'
        self.language = 'EN'
        self.languageDict = {}
        
        self.familyTreeName = 'My Family Tree'
        self.persons = []
        self.relations = []
        

        Builder.load_file('custom_widgets.kv')

        #parent_width = self.root.width
        #parent_width_dp = dp(parent_width/2)
        #print(f"Parent layout width: {parent_width} pixels, {parent_width_dp} dp")
        #self.ids.segment_control.ids.segment_panel.width = parent_width_dp

    def setLanguage(self, lang):
        if self.language == lang.upper():
            return
        
        if lang.upper() != 'EN':
            import csv
            data = {}
            file_path = f'languages/{lang.lower()}.csv'  # Verwendung einer f-string für den Dateipfad
            with open(file_path, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    key, value = row
                    data[key] = value
            self.languageDict = data
        else:
            self.languageDict = {}
        
        self.language = lang.upper()

        # Bildschirme neu laden
        screen_manager = self.root
        current_screen_name = screen_manager.current
        current_screens = [(screen.name, type(screen)) for screen in screen_manager.screens]

        for screen in screen_manager.screens[:]:
            screen_manager.remove_widget(screen)

        for name, cls in current_screens:
            screen_manager.add_widget(cls(name=name))

        screen_manager.current = current_screen_name

        print('reloaded language')

    def t(self, key):
        return self.languageDict.get(key, key) if self.language != 'EN' else key

    def getLanguage(self):
        return self.language

    def add_person(self, person):
        self.persons.append(person)

    def set_tree_name(self, name):
        self.familyTreeName = name

    def remove_person(self, id):
        for person in self.persons:
            if person.id == id:
                self.persons.remove(person)

    def print_persons(self):
        for person in self.persons:
            print(person)

    def save(self):
        treeJSON = jsonpickle.encode((self.familyTreeName, self.persons, self.relations), unpicklable=True)
        with open('persons.json', 'w') as fp:
            fp.write(treeJSON)
        
    def load_persons(self):
        if os.path.isfile('persons.json'):
            with open('persons.json', 'r') as fp:
                treeJSON = fp.read()
                (self.familyTreeName, self.persons, self.relations) = jsonpickle.decode(treeJSON)
        else:
            print("File 'persons.json' does not exist.")

if __name__ == "__main__":
    familyTreeApp().run()
