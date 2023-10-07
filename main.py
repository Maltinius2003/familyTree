import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


kivy.require('2.2.1')

class MyRoot(BoxLayout):
    def __init__(self): #Konstruktor
        super(MyRoot, self).__init__()

    def button(self):
        self.testLabel.text = 'asd'


class startupWindow(App):
    def build(self):
        return MyRoot()
    
startupWindow = startupWindow()
startupWindow.run()