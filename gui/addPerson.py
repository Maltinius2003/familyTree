from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

import helpMethods as hm

class AddPersonPopup(Popup):

    def __init__(self, religions, **kwargs):
        super(AddPersonPopup, self).__init__(**kwargs)
        self.title = 'Add Person'
        self.size_hint = (None, None)
        self.size = (800, 500)
        self.auto_dismiss = False

        # Übergabeparameter
        self.religions = religions

        # Create TextInput fields
        self.firstName = TextInput(multiline=False, hint_text='First Name')
        self.secondNames = TextInput(multiline=False, hint_text='Second Names')
        self.familyName = TextInput(multiline=False, hint_text='Family Name')
        self.academicDegree = TextInput(multiline=False, hint_text='Academic Degree')

        # Create Dropdowns for birthdate
        self.birth_day_dropdown = self.create_dropdown_button('Day', list(map(str, range(1, 32))))
        self.birth_month_dropdown = self.create_dropdown_button('Month', list(map(str, range(1, 13))))
        self.birth_year_input = TextInput(multiline=False, hint_text='Year')

        # Create Dropdowns for deathdate
        self.death_day_dropdown = self.create_dropdown_button('Day', list(map(str, range(1, 32))))
        self.death_month_dropdown = self.create_dropdown_button('Month', list(map(str, range(1, 13))))
        self.death_year_input = TextInput(multiline=False, hint_text='Year')

        transposed_mainReligion = hm.transpose_list(self.religions[0])
        self.mainReligion_dropdown = self.create_dropdown_button('Religion', transposed_mainReligion[-1])

        # Create Buttons
        cancel_button = Button(text='Cancel', on_press=self.dismiss)
        add_button = Button(text='Add', on_press=self.add_person)

        # Create GridLayout and add widgets
        popupLayout = GridLayout(cols=2, spacing=5, padding=10)
        popupLayout.add_widget(Label(text='First Name:'))
        popupLayout.add_widget(self.firstName)

        popupLayout.add_widget(Label(text='Second Names:'))
        popupLayout.add_widget(self.secondNames)

        popupLayout.add_widget(Label(text='Family Name:'))
        popupLayout.add_widget(self.familyName)

        popupLayout.add_widget(Label(text='Academic Degree:'))
        popupLayout.add_widget(self.academicDegree)

        popupLayout.add_widget(Label(text='Birthdate:'))
        birthdateLayout = GridLayout(cols=3, spacing=10, padding=10)
        birthdateLayout.add_widget(self.birth_day_dropdown)
        birthdateLayout.add_widget(self.birth_month_dropdown)
        birthdateLayout.add_widget(self.birth_year_input)
        popupLayout.add_widget(birthdateLayout)

        popupLayout.add_widget(Label(text='Deathdate:'))
        deathdateLayout = GridLayout(cols=3, spacing=10, padding=10)
        deathdateLayout.add_widget(self.death_day_dropdown)
        deathdateLayout.add_widget(self.death_month_dropdown)
        deathdateLayout.add_widget(self.death_year_input)
        popupLayout.add_widget(deathdateLayout)

        popupLayout.add_widget(Label(text='Religion:'))
        popupLayout.add_widget(self.mainReligion_dropdown)
        
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
            f"Birthdate: {self.birth_day_dropdown.text}/{self.birth_month_dropdown.text}/{self.birth_year_input.text}\n"
            f"Deathdate: {self.death_day_dropdown.text}/{self.death_month_dropdown.text}/{self.death_year_input.text}"
        )
        print(f"Adding person with info:\n{person_info}")
        self.dismiss()