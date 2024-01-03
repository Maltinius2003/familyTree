from kivy.app import App
from kivy.uix.screenmanager import Screen

class ShowFamilyTreeScreen(Screen):
    def screen_method(self):
        print('Hello from showfamilytree')
        # self.manager.get_screen('menu').screen_method()  # sample how to call other screen method from here
        # self.manager.screen_manager_method()  # sample how to call screen manager method from here
        # App.get_running_app().app_method()  # sample hot to call app method from here
