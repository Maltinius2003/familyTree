from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

import gui.addPerson

class Root(GridLayout):

    def __init__(self, religions, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.cols = 1
        self.religions = religions
        self.add_widget(Label(text='Family Tree App', font_size=50))
        self.add_widget(Button(text='Select Family Tree', font_size=20, on_press=self.select_family_tree))
        self.add_widget(Button(text='Add Person', font_size=20, on_press=self.add_person))
        self.add_widget(Button(text='Settings', font_size=20, on_press=self.open_settings))
        self.add_widget(Button(text='Exit', font_size=20, on_press=self.exit_app))

    def select_family_tree(self, instance):
        print("Select Family Tree")
        #print(self.religions)

    def add_person(self, instance):
        print("Add Person")
        popup = gui.addPerson.AddPersonPopup(self.religions)
        popup.open()

    def open_settings(self, instance):
        print("Open Settings")

    def exit_app(self, instance):
        print("Exit")
        App.get_running_app().stop()


