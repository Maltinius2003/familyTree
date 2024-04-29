from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineListItem
from kivy.app import App
    
class AddFamilyTreeScreen(Screen):
    gender = StringProperty('u') # StringProperty nesserary to get the button state updated
    firstName = StringProperty('') 
    secondNames = StringProperty('')
    lastName = StringProperty('')


    def __init__(self, **kwargs):
        #self.gender = 'u'
        super().__init__(**kwargs)


    def screen_method(self):
        print('Hello from addfamilytree')

    def checkFirstName(self, instance):
        # Only allow alphanumeric characters and dashes
        cleaned_text = ''
        #print(instance.text)
        for ch in instance.text:
            if ch.isalpha() or ch == '-':
                cleaned_text += ch

        # Update the instance text with the cleaned text
        instance.text = cleaned_text

    def checkSecondNames(self, instance):
        # Only allow alphanumeric characters, dashes, and spaces, no space-space, dash-space, space-dash, or dash-dash
        cleaned_text = ''
        previous_char = ''
        for i, ch in enumerate(instance.text):
            if i == 0 and (ch == '-' or ch == ' '):
                continue
            if ch.isalpha() or ch == '-' or ch == ' ':
                if ch == ' ' and previous_char == '-':
                    continue
                if ch == '-' and previous_char == ' ':
                    continue
                if ch == '-' and previous_char == '-':
                    continue
                if ch == ' ' and previous_char == ' ':
                    continue
                cleaned_text += ch
                previous_char = ch

        # Update the instance text with the cleaned text
        instance.text = cleaned_text

    def checkDashOrSpaceAtEnd(self, instance):
        # Check if the last character is a dash or space, if so, throw an error
        if instance.text[-1:] == '-' or instance.text[-1:] == ' ':
            instance.error = True

    def checkLastName(self, instance):
        self.checkSecondNames(instance)

    def setGender(self, gender):
        self.gender = gender
        #print(self.gender)

    def test(self):
        print('test')
    
    def show_day_menu(self):
        days = [App.get_running_app().t('Unknown')] + [str(day) for day in range(1, 32)]
        menu_items = [{"viewclass": "OneLineListItem", "text": day, "on_release": lambda day=day, day_number=days.index(day): self.set_day({"text": day, "number": day_number})} for day in days]
        self.day_menu = MDDropdownMenu(
            caller=self.ids.day_button,
            items=menu_items,
            position="auto"
        )
        self.day_menu.open()

    def set_day(self, item):
        if item['number'] == 0:
            self.ids.day_button.text = App.get_running_app().t('Day')
            self.ids.day_button.theme_text_color = 'Secondary'
        else:
            self.ids.day_button.text = item['text']
            self.ids.day_button.theme_text_color = 'Primary'
        print(f'Selected day: {item["text"]}, number: {item["number"]}')
        self.day_menu.dismiss()

    def show_month_menu(self):
        months = ['Unknown', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        translated_months = [App.get_running_app().t(month) for month in months]
        menu_items = [{"viewclass": "OneLineListItem", "text": month, "on_release": lambda month=month, month_number=translated_months.index(month): self.set_month({"text": month, "number": month_number})} for month in translated_months]
        self.month_menu = MDDropdownMenu(
            caller=self.ids.month_button,
            items=menu_items,
            position="auto"
        )
        self.month_menu.open()
    
    def set_month(self, item):
        if item['number'] == 0: 
            self.ids.month_button.text = App.get_running_app().t('Month')
            self.ids.month_button.theme_text_color = 'Secondary'
        else:
            self.ids.month_button.text = item['text']
            self.ids.month_button.theme_text_color = 'Primary'
        print(f'Selected month: {item["text"]}, number: {item["number"]}')
        self.month_menu.dismiss()

    



         
            


        

