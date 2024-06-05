from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp

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
        
        self.persons = []

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

    def remove_person(self, id):
        for person in self.persons:
            if person.id == id:
                self.persons.remove(person)
        

if __name__ == "__main__":
    familyTreeApp().run()
