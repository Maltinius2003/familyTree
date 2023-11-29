from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
#from kivy.uix.layout import RootLayout


class MyApp(App):
    def build(self):
        return RootLayout()

    def open_dataset(self):
        print("open dataset")

    def create_person(self):
        print("create person")

    def open_settings(self):
        print("open settings")

if __name__ == '__main__':
    MyApp().run()
