from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

class Root(GridLayout):

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Family Tree App', font_size=50))
        self.add_widget(Button(text='Select Family Tree', font_size=20, on_press=self.select_family_tree))
        self.add_widget(Button(text='Add Person', font_size=20, on_press=self.add_person))
        self.add_widget(Button(text='Settings', font_size=20, on_press=self.open_settings))
        self.add_widget(Button(text='Exit', font_size=20, on_press=self.exit_app))
        

    def select_family_tree(self, instance):
        print("Select Family Tree")

    def add_person(self, instance):
        print("Add Person")
        popup = AddPersonPopup()
        popup.open()

    def open_settings(self, instance):
        print("Open Settings")

    def exit_app(self, instance):
        print("Exit")
        App.get_running_app().stop()

class AddPersonPopup(Popup):

    def __init__(self, **kwargs):
        super(AddPersonPopup, self).__init__(**kwargs)
        self.title = 'Add Person'
        self.size_hint = (None, None)
        self.size = (500, 300)
        self.auto_dismiss = False

        # Create TextInput fields
        self.firstName = TextInput(multiline=False, hint_text='First Name')
        self.secondNames = TextInput(multiline=False, hint_text='Second Names')
        self.familyName = TextInput(multiline=False, hint_text='Family Name')
        self.academicDegree = TextInput(multiline=False, hint_text='Academic Degree')

        # Create Dropdowns for birthdate
        self.day_dropdown = self.create_dropdown_button('Day', list(map(str, range(1, 32))))
        self.month_dropdown = self.create_dropdown_button('Month', list(map(str, range(1, 13))))
        self.year_input = TextInput(multiline=False, hint_text='Year')

        # Create Buttons
        cancel_button = Button(text='Cancel', on_press=self.dismiss, size_hint=(None, None), height=30)
        add_button = Button(text='Add', on_press=self.add_person, size_hint=(None, None), height=30)

        # Create GridLayout and add widgets
        popupLayout = GridLayout(cols=2, spacing=10, padding=10)
        popupLayout.add_widget(Label(text='First Name:'))
        popupLayout.add_widget(self.firstName)

        popupLayout.add_widget(Label(text='Second Names:'))
        popupLayout.add_widget(self.secondNames)

        popupLayout.add_widget(Label(text='Family Name:'))
        popupLayout.add_widget(self.familyName)

        popupLayout.add_widget(Label(text='Academic Degree:'))
        popupLayout.add_widget(self.academicDegree)

        popupLayout.add_widget(Label(text='Birthdate:'))
        popupLayout.add_widget(self.day_dropdown)
        popupLayout.add_widget(self.month_dropdown)
        popupLayout.add_widget(self.year_input)
        
        popupLayout.add_widget(cancel_button)
        popupLayout.add_widget(add_button)

        # Set popupLayout as content of the Popup
        self.content = popupLayout

    def create_dropdown_button(self, text, values):
        dropdown = Button(text=text, size_hint=(None, None), height=30)
        dropdown.bind(on_release=lambda btn: self.show_dropdown(values, btn))
        return dropdown

    def show_dropdown(self, values, button):
        dropdown = DropDown()

        for value in values:
            btn = Button(text=value, size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        dropdown.bind(on_select=lambda instance, x: setattr(button, 'text', x))
        dropdown.open(button)

    def add_person(self, instance):
        person_info = (
            f"First Name: {self.firstName.text}\n"
            f"Second Names: {self.secondNames.text}\n"
            f"Family Name: {self.familyName.text}\n"
            f"Academic Degree: {self.academicDegree.text}\n"
            f"Birthdate: {self.day_dropdown.text}/{self.month_dropdown.text}/{self.year_input.text}"
        )
        print(f"Adding person with info:\n{person_info}")
        self.dismiss()

class MyApp(App):

    def build(self):
        return Root()

if __name__ == '__main__':
    MyApp().run()
