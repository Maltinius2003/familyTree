from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.pickers import MDModalInputDatePicker

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDButton:
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_date_picker()

        MDButtonText:
            text: "Open modal date picker dialog"
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)

    def show_date_picker(self):
        date_dialog = MDModalInputDatePicker()
        date_dialog.open()


Example().run()