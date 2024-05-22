from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp

KV = '''
ScreenManager:
    AddFamilyTreeScreen:

<AddFamilyTreeScreen>:
    name: 'addfamilytree'

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        MDTopAppBar:
            title: "Add Initial Family Member"
            left_action_items: [['arrow-left', lambda x: None]]
            elevation: 10
            size_hint_y: None
            height: dp(56)  # Feste Höhe für die Toolbar

        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)

                MDTextField:
                    hint_text: "First Name"
                    size_hint_y: None
                    height: dp(48)  # Feste Höhe für das Textfeld

                MDTextField:
                    hint_text: "Second Name"
                    size_hint_y: None
                    height: dp(48)  # Feste Höhe für das Textfeld

                MDTextField:
                    hint_text: "Last Name"
                    size_hint_y: None
                    height: dp(48)  # Feste Höhe für das Textfeld

                MDTextField:
                    hint_text: "Last Name"
                    size_hint_y: None
                    height: dp(48)  # Feste Höhe für das Textfeld

                MDTextField:
                    hint_text: "Last Name"
                    size_hint_y: None
                    height: dp(48)  # Feste Höhe für das Textfeld

                MDTextField:
                    hint_text: "Last Name"
                    size_hint_y: None
                    height: dp(48)  # Feste Höhe für das Textfeld

                MDTextField:
                    hint_text: "Last Name"
                    size_hint_y: None
                    height: dp(48)  # Feste Höhe für das Textfeld

                MDTextField:
                    hint_text: "Last Name"
                    size_hint_y: None
                    height: dp(48)  # Feste Höhe für das Textfeld

                MDTextField:
                    hint_text: "Last Name"
                    size_hint_y: None
                    height: dp(48)  # Feste Höhe für das Textfeld

                MDTextField:
                    hint_text: "Last Name"
                    size_hint_y: None
                    height: dp(48)  # Feste Höhe für das Textfeld

                MDTextField:
                    hint_text: "Last Name"
                    size_hint_y: None
                    height: dp(48)  # Feste Höhe für das Textfeld

                MDTextField:
                    hint_text: "Last Name"
                    size_hint_y: None
                    height: dp(48)  # Feste Höhe für das Textfeld

                MDRectangleFlatButton:
                    text: "Back"
                    pos_hint: {'center_x': 0.5}
                    on_press: app.on_back_button()
                    size_hint_y: None
                    height: dp(48)  # Feste Höhe für den Button
'''

class AddFamilyTreeScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_back_button(self):
        # Logic for the back button can be added here
        print("Back button pressed")

MainApp().run()
