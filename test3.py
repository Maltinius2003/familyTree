from kivy.lang import Builder

from kivymd.app import MDApp

from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
FloatLayout:
    MDCheckbox:
        pos_hint: {'center_x': .75, 'center_y': .5}
        size_hint: None, None
        size: dp(48), dp(48)
    MDLabel:
        text: "Checkbox Label"
        pos_hint: {'center_x': .55, 'center_y': .5}
'''

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()