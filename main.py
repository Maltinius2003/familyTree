from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty

import showfamilytree, menu, addfamilytree, settings


# hierarhy:
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
        self.title = 'Family Tree App'
        self.language = 'EN'
        self.languageDict = {}
        
        super().__init__(**kwargs)

        #self.setLanguage('EN')

    def setLanguage(self, lang):
        if self.language == lang.upper():
            return
        if lang.upper() != 'EN':
            import csv
            data = {}
            file_path = 'languages/' + lang.lower() + '.csv'
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    key = row[0]
                    value = row[1]
                    data[key] = value
            self.languageDict = data
            self.language = lang.upper()
        else:
            self.language = 'EN'
            self.languageDict = {}

        #Reload the screens
        # Get the instance of the ScreenManager
        screen_manager = self.root
        # Remember the name of the current screen
        current_screen_name = screen_manager.current
        # Create a list of the current screens
        current_screens = [(screen.name, type(screen)) for screen in screen_manager.screens]
        # Remove all screens
        for screen in screen_manager.screens[:]:
            screen_manager.remove_widget(screen)
        # Add the original screens back
        for name, cls in current_screens:
            screen_manager.add_widget(cls(name=name))
        # Switch back to the original screen
        screen_manager.current = current_screen_name

        print('reloaded language')

    def t(self, key):
        if self.language == 'EN':
            return key
        else:
            return self.languageDict.get(key, key)

    def getlanguage(self):
        return self.language    

familyTreeApp().run()