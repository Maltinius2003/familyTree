from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
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
    def app_method(self):
        print('Hello from app')

familyTreeApp().run()