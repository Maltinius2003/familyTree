from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch

KV = '''
OneLineAvatarIconListItem:
    text: "Language"
    on_size:
        self.ids._right_container.width = container.width
        self.ids._right_container.x = container.width

    IconLeftWidget:
        icon: "flag"

    YourContainer:
        id: container

        MDIconButton:
            id: button
            icon: "language-python"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.dropdown1.open()
'''


class YourContainer(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Example().run()