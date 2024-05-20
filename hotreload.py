from kaki.app import App
from kivy.factory import Factory
from kivymd.app import MDApp
import os

class Live(App, MDApp):  # Hier beide Klassen erben
    CLASSES = {
        'MyScreens': 'main',  # Die Klasse MyScreens ist in der main.py definiert
    }

    KV_FILES = {
        os.path.join(os.getcwd(), 'familyTreeApp.kv'),
        os.path.join(os.getcwd(), 'menu.kv'),
        os.path.join(os.getcwd(), 'showfamilytree.kv'),
        os.path.join(os.getcwd(), 'addfamilytree.kv'),
        os.path.join(os.getcwd(), 'settings.kv')
    }

    AUTORELOADER_PATHS = [
        ('.', {'recursive': True}),  # Rekursives Hot-Reloading im aktuellen Verzeichnis
    ]

    def build_app(self, first=False):
        print('build_app')
        return Factory.MyScreens()

if __name__ == '__main__':
    Live().run()
