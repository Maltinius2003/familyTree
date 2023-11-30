from kivy.app import App

import initialize
import gui.root

global religions

class MyApp(App):

    def build(self):
        return gui.root.Root(religions)

if __name__ == '__main__':
    religions = initialize.importReligions()
    MyApp().run()
    