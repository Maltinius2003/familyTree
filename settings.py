from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.app import App
from kivymd.uix.button import MDFlatButton

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        self.languageList = self.lookForLanguages()
        self.languageList.append('EN')
        self.languageList.sort()
        self.langItems = [
            {
                "viewclass": "OneLineListItem",
                "text": language,
                "on_release": lambda x=language: self.dropLangCallback(x),
            } for language in self.languageList
        ]
        

        self.dropLang = MDDropdownMenu(items=self.langItems, width_mult=4)
        super().__init__(**kwargs)

    def lookForLanguages(self):
        import os
        languages = []
        for file in os.listdir('languages'):
            if file.endswith('.csv'):
                languages.append(file[:-4].upper())
        return languages # returns a list of languages
    
    def dropdownLanguages(self, button):
        self.dropLang.caller = button
        self.dropLang.open()

    def dropLangCallback(self, x):
        App.get_running_app().setLanguage(x)