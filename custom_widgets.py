from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivymd.uix.menu import MDDropdownMenu
from kivy.app import App
from kivy.properties import ObjectProperty

class CustomLabels(BoxLayout):
    pass

class CustomDateWidget(BoxLayout):

    title = StringProperty("test_title")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.day = None
        self.month = None
        self.year = None
        self.bc = False
    
    '''
    title = StringProperty("test_title")
    day = None
    month = 0
    year = -1
    bc = False'''

    first_use_day = True # error when set_day() is used before menu is opened 

    def show_day_menu(self):
        days = [App.get_running_app().t('Unknown')] + [str(day) for day in range(1, 32)]
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": day,
                "on_release": lambda day=days.index(day): self.set_day(day)
            }
            for day in days
        ]
        self.day_menu = MDDropdownMenu(
            caller=self.ids.day_button,
            items=menu_items,
            position="auto"
        )
        self.day_menu.open()
        self.first_use_day = False

    def set_day(self, item):
        day = item
        if day == 0:
            self.ids.day_button.text = App.get_running_app().t('Day')
            self.ids.day_button.theme_text_color = 'Secondary'
            self.day = None
        else:
            day = self.check_day(day)
            self.ids.day_button.text = str(day)
            self.ids.day_button.theme_text_color = 'Primary'
            self.day = day
             
        if not self.first_use_day:
            self.day_menu.dismiss()

    def show_month_menu(self):
        months = ['Unknown', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        if App.get_running_app().getLanguage().upper() != 'EN':
            months = [App.get_running_app().t(month) for month in months]
        
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": month,
                "on_release": lambda month=months.index(month), month_name=month: self.set_month(month, month_name)
            }
            for month in months
        ]
        self.month_menu = MDDropdownMenu(
            caller=self.ids.month_button,
            items=menu_items,
            position="auto"
        )
        self.month_menu.open()
    
    def set_month(self, month, month_name):
        if month == 0: 
            self.ids.month_button.text = App.get_running_app().t('Month')
            self.ids.month_button.theme_text_color = 'Secondary'
        else:
            self.ids.month_button.text = month_name
            self.ids.month_button.theme_text_color = 'Primary'
        #print(f'Selected month: {month_name}({month})') #pass everytime, to set the month, could be changed back to unknown
        if month is 0:
            self.month = None
        else:
            self.month = month
        if self.day is not None: self.set_day(self.day) #check if the day is still valid
        self.month_menu.dismiss()

    def check_day(self, day):
        # restrctions only after year 8ad, first sure leap year after Augustus corrects the calendar
        if not self.bc and self.year is not None and self.year >= 8:
            if self.month == 2 and day > 28: #february problem
                if self.year > 1582: # > since 1582ad gregorian calendar
                    if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
                        return 29 #gregorian leap year
                    else:
                        return 28 #gregorian common year
                elif self.year <= 1582: # 8ad - 1582ad, safe julian calendar, 8 ad is the first common leap year, before that there were mistakes
                    if self.year % 4 == 0:
                        return 29 #julian leap year 
                    else:
                        return 28 #julian common year
                else:
                    return day # facts before 8ad are not clear, allow every day
            elif self.month in [4, 6, 9, 11] and day > 30:
                return 30
            elif self.year == 1582 and self.month == 10 and day > 4 and day < 15: # 5th - 14th October 1582 does not exist
                return 4
        return day
        
    def set_year(self, instance):
        new_year = instance.text
        if not new_year == '':
            if new_year == '0':
                new_year = '1' #year 0 does not exist in the historic context 
                instance.text = new_year
            self.year = int(new_year)
            if self.day is not None: self.set_day(self.day) #check if the day is still valid
        else:
            self.year = None

    def set_bc(self, bc):
        self.bc = bc
        #print(self.bc)

    def test2():
        print('test2')
