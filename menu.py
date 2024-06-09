from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem

class MenuScreen(Screen):
    def screen_method(self):
        print('Hello from menu')

    def on_start(self):
        for i in range(20):
            self.root.ids.container.add_widget(
                OneLineListItem(text=f"Single-line item {i}")
            )